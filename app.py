from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine
from pymongo import MongoClient
import logging
from flask_cors import CORS
from dotenv import load_dotenv
import os


load_dotenv()


app = Flask(__name__)
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG')
CORS(app)

@app.route('/')
def index():        
    return 'Hello World'


app.run()