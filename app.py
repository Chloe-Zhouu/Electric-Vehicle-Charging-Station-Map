from flask import Flask, render_template


app = Flask(__name__)

# Home page
@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/charts')
# def charts():
#     return render_template('charts.html')


