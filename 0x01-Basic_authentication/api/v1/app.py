#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


# Create a Flask application and configure CORS settings
app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Initialize a variable based on the environment variable AUTH_TYPE
auth = None
auth_type = getenv('AUTH_TYPE')

# Instantiate the appropriate authentication class based on AUTH_TYPE
if auth_type == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
else:
    from api.v1.auth.auth import Auth
    auth = Auth()

# Define a list of paths that don't need authentication
excluded_paths = [
    '/api/v1/status/',
    '/api/v1/unauthorized/',
    '/api/v1/forbidden/']


@app.before_request
def before_request():
    """Filter and authenticate incoming API requests.
    """
    if auth is None:
        pass

    current_path = request.path

    if auth.require_auth(current_path, excluded_paths):
        authorization_header = auth.authorization_header(request)
        current_user = auth.current_user(request)

        if authorization_header is None:
            abort(401, description="Unauthorized")

        if current_user is None:
            abort(403, description="Forbidden")


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized_error(e) -> str:
    """Custom Unauthorized error handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden_error(e) -> str:
    """Custom Forbidden error handler
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
