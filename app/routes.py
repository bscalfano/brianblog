from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, I hope this works!"