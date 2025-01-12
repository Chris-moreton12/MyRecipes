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
