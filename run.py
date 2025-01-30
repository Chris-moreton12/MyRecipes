import os
from flask import Flask, render_template, request, redirect, url_for, session
from flask_bcrypt import Bcrypt
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secures random secret key for sessions
bcrypt = Bcrypt(app)

# MongoDB connection string 
client = MongoClient('mongodb+srv://Chris:Cmoreton3912@myrecipe.95tdx.mongodb.net/recipe_app?retryWrites=true&w=majority&appName=Myrecipe')
db = client['recipe_app']
users_collection = db['users']
recipes_collection = db['recipes']

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if 'user_id' in session:  # Redirect if already logged in
        return redirect(url_for('dashboard'))

    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        security_question_1 = request.form['security_question_1']
        security_question_2 = request.form['security_question_2']

        # Validate the username and password
        if len(username) < 3:
            error = "Username must be at least 3 characters long."
        elif len(password) < 6:
            error = "Password must be at least 6 characters long."
        elif users_collection.find_one({'username': username}):
            error = "Username already exists. Please choose another."
        else:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

            # Insert the new user into the database
            users_collection.insert_one({
                'username': username,
                'password': hashed_password,
                'security_question_1': security_question_1,
                'security_question_2': security_question_2
            })
            return redirect(url_for('login'))

    return render_template('signup.html', error=error)  # Pass error message to the template

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if 'user_id' in session:  # Redirect if already logged in
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Fetch user from the database
        user = users_collection.find_one({'username': username})
        if user and bcrypt.check_password_hash(user['password'], password):
            session['user_id'] = str(user['_id'])
            session['username'] = username
            return redirect(url_for('dashboard'))

        error = "Invalid username or password. Please try again."

    return render_template('login.html', error=error)

# Reset password link
@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        answer_1 = request.form['security_question_1']
        answer_2 = request.form['security_question_2']

        # Fetch user and validate the security questions
        user = users_collection.find_one({'username': username})
        if user and user['security_question_1'] == answer_1 and user['security_question_2'] == answer_2:
            # Allow the user to reset their password
            return redirect(url_for('reset_password', username=username))
        else:
            error = "Incorrect username or security answers. Please try again."

    return render_template('forgot_password.html' , error=error)

# Added functionality to reset the password after validating security questions
@app.route('/reset_password/<username>', methods=['GET', 'POST'])
def reset_password(username):
    if request.method == 'POST':
        new_password = request.form['new_password']

        # Update the user's password
        hashed_password = bcrypt.generate_password_hash(new_password).decode('utf-8')
        users_collection.update_one(
            {'username': username},
            {'$set': {'password': hashed_password}}
        )
        return redirect(url_for('login'))

    return render_template('reset_password.html', username=username)


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        # Create a new recipe
        title = request.form['title']
        content = request.form['content']

        # Ensure title and content are provided
        if not title or not content:
            return "Title and content are required."

        recipes_collection.insert_one({
            'user_id': session['user_id'],
            'title': title,
            'content': content
        })

    # Retrieve all recipes for the logged-in user
    user_recipes = recipes_collection.find({'user_id': session['user_id']})
    return render_template('dashboard.html', username=session['username'], recipes=user_recipes)

@app.route('/edit/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    # Convert string recipe_id to ObjectId
    recipe = recipes_collection.find_one({'_id': ObjectId(recipe_id), 'user_id': session['user_id']})
    if not recipe:
        return "Recipe not found."

    if request.method == 'POST':
        # Update the recipe
        new_title = request.form['title']
        new_content = request.form['content']

        # Ensure title and content are provided
        if not new_title or not new_content:
            return "Title and content are required."

        recipes_collection.update_one(
            {'_id': ObjectId(recipe_id), 'user_id': session['user_id']},
            {'$set': {'title': new_title, 'content': new_content}}
        )
        return redirect(url_for('dashboard'))

    return render_template('edit.html', recipe=recipe)

@app.route('/delete/<recipe_id>', methods=['POST'])
def delete_recipe(recipe_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    # Delete the recipe
    recipes_collection.delete_one({'_id': ObjectId(recipe_id), 'user_id': session['user_id']})
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
