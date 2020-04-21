#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, request_tearing_down, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_list(id=None):
    states = storage.all("State")
    cities = storage.all("City").values()
    if id is not None:
        id = "State." + id
    print (id)
    return render_template("9-states.html",
                           states=states, cities=cities, id=id)


@app.teardown_appcontext
def teardown_db(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
