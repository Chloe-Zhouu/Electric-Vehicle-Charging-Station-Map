from flask import Flask, render_template


app = Flask(__name__)

# Home page
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/car')
def car():
    return render_template('cars.html')