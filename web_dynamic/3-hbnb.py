#!/usr/bin/python3
""" Starts a Flask Web Application """
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
import uuid

app = Flask(__name__)

@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()

@app.route('/3-hbnb', strict_slashes=False)
def hbnb():
    """ HBNB is alive! """
    # Query all States from storage, sort them by name and append
    # their cities, sorted by name, to a list.
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []
    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    # Query all Amenities and sort them by name.
    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    # Query all Places and sort them by name.
    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    # Render the HTML template, passing it the sorted States, Amenities
    # and Places lists, as well as a cache id.
    return render_template('3-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
                           cache_id=uuid.uuid4())

if __name__ == "__main__":
    """ Main Function """
    app.run(debug=True, host='0.0.0.0', port=5000)
