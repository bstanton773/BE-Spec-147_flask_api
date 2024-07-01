import os
from flask import Flask # Import the Flask class from the flask library
from app.database import db # Import the instance of SQLAlchemy (db) from database module


# Create an instance of the flask application
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///advanced_ecommerce.db'

# Initialize the app with the flask-sqlalchemy
db.init_app(app)

# Import the routes file so that it runs
from . import routes
