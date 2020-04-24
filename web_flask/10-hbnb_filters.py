#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, request_tearing_down, render_template
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def states_list(id=None):
    """send states, cities and amenities"""
    states = storage.all("State").values()
    cities = storage.all("City").values()
    amenities = storage.all("Amenity").values()
    return render_template("10-hbnb_filters.html",
                           states=states, cities=cities, amenities=amenities)


@app.teardown_appcontext
def teardown_db(self):
    """Teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
