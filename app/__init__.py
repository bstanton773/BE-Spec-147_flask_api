import os
from flask import Flask # Import the Flask class from the flask library
from app.database import db, migrate # Import the instance of SQLAlchemy (db) and instance of Migrate (migrate) from database module
from app.limiter import limiter
from app.caching import cache
from app.swagger_docs import swaggerui_blueprint


# Create an instance of the flask application
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///advanced_ecommerce.db'

# Initialize the app with the flask-sqlalchemy
db.init_app(app)

# Initialize the app and db with migrate
migrate.init_app(app, db)

# Initialize the app with flask-limiter
limiter.init_app(app)

# Initialize the app with flask-caching
cache.init_app(app)

# Register the Swagger UI Blueprint
app.register_blueprint(swaggerui_blueprint)

# Import the routes file so that it runs
from . import routes, models
