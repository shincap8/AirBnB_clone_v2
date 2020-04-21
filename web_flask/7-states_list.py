#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, request_tearing_down, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all("State").values()
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_db(self):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
