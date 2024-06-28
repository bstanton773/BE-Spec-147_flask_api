from app import app # from the app folder, import the app variable (Flask instance)

@app.route('/')
def index():
    return 'Goodbye'
