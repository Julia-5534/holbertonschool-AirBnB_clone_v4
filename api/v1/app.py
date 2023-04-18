#!/usr/bin/python3
""" Flask Application """
from models import storage
from api.v1.views import app_views
from os import environ
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from

# Initialize the Flask app
app = Flask(__name__)
# Set configuration options for Flask
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
# Register the blueprint for the views
app.register_blueprint(app_views)
# Enable CORS for the app
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


# Define a funct to close the database conn when the app is done
@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()


# Define an error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
# Define the response to send back for 404 errors
    return make_response(jsonify({'error': "Not found"}), 404)


# Set configuration options for the Swagger documentation
app.config['SWAGGER'] = {
    'title': 'AirBnB clone Restful API',
    'uiversion': 3
}

# Initialize the Swagger documentation for the app
Swagger(app)


# Start the app if this is the main script being run
if __name__ == "__main__":
    # Get the host and port conf. options from env. var, or use defaults
    """ Main Function """
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'

    # Start the Flask app
    app.run(host=host, port=port, threaded=True)
