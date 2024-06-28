from flask import Flask # Import the Flask class from the flask library


# Create an instance of the flask application
app = Flask(__name__)


@app.route('/')
def index():
    return 'Goodbye'

