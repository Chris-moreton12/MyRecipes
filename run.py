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
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Validate the username and password
        if len(username) < 3 or len(password) < 6:
            return "Username must be at least 3 characters and password must be at least 6 characters."

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Check if the username already exists
        if users_collection.find_one({'username': username}):
            return "Username already exists. Please choose another."

        # Insert the new user into the database
        users_collection.insert_one({'username': username, 'password': hashed_password})
        return redirect(url_for('login'))

        return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Fetch user from the database
        user = users_collection.find_one({'username': username})
        if user and bcrypt.check_password_hash(user['password'], password):
            session['user_id'] = str(user['_id'])
            session['username'] = username
            return redirect(url_for('dashboard'))

        return "Invalid username or password."

    return render_template('login.html')

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


