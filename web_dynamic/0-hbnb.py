#!/usr/bin/python3

""" Starts a Flask Web Application """

# Import necessary modules and classes from the
# models file, as well as other modules
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
import uuid

# Initialize the Flask app
app = Flask(__name__)

# Define a function to remove the current SQLAlchemy
# session when the app context is torn down
@app.teardown_appcontext
def close_db(error):
    storage.close()

# Define a route for the homepage of the app
@app.route('/0-hbnb', strict_slashes=False)
def hbnb():
    # Retrieve data from the database and sort it as needed
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []
    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])
    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)
    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    # Render the homepage template with the retrieved data
    # and a cache ID generated using uuid.uuid4()
    return render_template('0-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
                           cache_id=uuid.uuid4())

# Start the app if this script is being run directly
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
