#!/usr/bin/env python3
"""
Flask application for user authentication service.
"""
from flask import Flask, jsonify, request, abort, make_response
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", strict_slashes=False)
def welcome():
    """Render a welcome message as a JSON response.

    Returns:
        dict: A JSON payload containing a welcome message.
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def register_user():
    """Register a new user.

    Returns:
        dict: A JSON payload containing the registration
        status.
    """
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        # Attempt to register a new user
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})

    except ValueError:
        # Handle the case where the email is already registered
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login():
    """Handle user login.

    Returns:
        Flask response: JSON payload with user information
        and a session ID cookie.
        HTTP status codes:
            200 - Successful login.
            401 - Unauthorized if login information is incorrect.
            500 - Internal Server Error for other exceptions.
    """
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        if AUTH.valid_login(email, password):
            # Login successful, create a new session
            session_id = AUTH.create_session(email)
            response_data = {"email": email, "message": "logged in"}
            response = make_response(jsonify(response_data), 200)
            response.set_cookie("session_id", session_id)
            return response
        else:
            # Incorrect login information
            abort(401)

    except ValueError as e:
        # Handle other exceptions if needed
        abort(500, str(e))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
