#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template

from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def states():
    """Get all state data"""
    data = storage.all("State")
    return render_template("9-states.html",
                           states=data)


@app.route('/states/<id>')
def states_by_id(id):
    """State by id"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html",
                                   id=id, state=state, notfound=False)
    return render_template("9-states.html", notfound=True)


@app.teardown_appcontext
def terminate(exc):
    """Close SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
