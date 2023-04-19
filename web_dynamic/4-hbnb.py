#!/usr/bin/python3
""" Starts a Flask Web Application """

# Importing required modules and classes
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
import uuid

# Creating a Flask app instance
app = Flask(__name__)

# Flask configuration
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# Close the current SQLAlchemy session when the context of the app is popped
@app.teardown_appcontext
def close_db(error):
    storage.close()

# Route that returns HTML template
@app.route('/4-hbnb', strict_slashes=False)
def hbnb():
    """ HBNB is alive! """

    # Retrieve all States and sort them alphabetically
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)

    # Create a list of each state and its cities, and sort
    # each city alphabetically
    st_ct = []
    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    # Retrieve all Amenities and sort them alphabetically
    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    # Retrieve all Places and sort them alphabetically
    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    # Return the HTML template with the relevant data
    return render_template('4-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
                           cache_id=uuid.uuid4())

# Main function that runs the app
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
