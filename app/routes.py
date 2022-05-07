from app import app
from flask import render_template, redirect
from app.forms import LocationForm
from app.dijkstra import *

import os
import json
from ipywidgets.embed import embed_minimal_html
import gmaps

MAPS_API_KEY = os.environ.get('MAPS_API_KEY')

gmaps.configure(api_key=MAPS_API_KEY)


@app.route('/')
@app.route('/index')
def index():
    form = LocationForm()
    data = {'starting_point': 'London, UK', 'ending_point': 'Hull, UK'}
    pts = json.dumps(['Leicester, UK'])
    return render_template('index.html', form=form, data=data, pts=pts)

@app.route('/map')
def map():
    return render_template('export.html')

@app.route('/login')
def login():
    return render_template('login.html')

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
