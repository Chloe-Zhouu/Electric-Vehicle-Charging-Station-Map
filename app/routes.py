from app import app
from flask import render_template, redirect, flash, url_for
from app.forms import LocationForm, LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.dijkstra import *
from app.models import User
import json

@app.route('/')
@app.route('/index')
@login_required
def index():
    form = LocationForm()
    data = {'starting_point': 'London, UK', 'ending_point': 'Hull, UK'}
    pts = json.dumps(['Leicester, UK'])
    return render_template('index.html', form=form, data=data, pts=pts)

@app.route('/map')
def map():
    return render_template('export.html')


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/location', methods=['GET','POST'])
def get_location():
    form = LocationForm()
    starting_point = form.start_location.data
    ending_point = form.end_location.data

    previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=starting_point)
    path = print_result(previous_nodes, shortest_path, start_node=starting_point, target_node=ending_point)
    data = {'starting_point': "{}, UK".format(path[0]), 'ending_point': "{}, UK".format(path[-1])}
    pts = json.dumps(["{}, UK".format(city) for city in path[1:-1]])
    return render_template('index.html', form=form, data=data, pts=pts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))