#!/usr/bin/env python3
"""
Flask application for user authentication service.
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def welcome():
    """Render a welcome message as a JSON response.

    Returns:
        dict: A JSON payload containing a welcome message.
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
