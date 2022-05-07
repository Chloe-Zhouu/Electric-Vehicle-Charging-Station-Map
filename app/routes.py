from app import app
from flask import render_template, redirect
from app.forms import LocationForm

import os
from ipywidgets.embed import embed_minimal_html
import gmaps

MAPS_API_KEY = os.environ.get('MAPS_API_KEY')

gmaps.configure(api_key=MAPS_API_KEY)


@app.route('/')
@app.route('/index')
def index():
    form = LocationForm()
    return render_template('index.html', form=form)

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
    # print("starting point: {} and ending point: {}".format(
    #         form.start_location.data, form.end_location.data))
    # print(type(form.start_location.data))
    marker_locations = [(float(form.start_location.data), float(form.end_location.data))]

    fig = gmaps.figure()
    markers = gmaps.marker_layer(marker_locations)
    fig.add_layer(markers)
    embed_minimal_html('app/templates/export.html', views=[fig])
    return redirect('/index')