#!/usr/bin/env python3
"""
Flask application for user authentication service.
"""
from flask import (
    Flask,
    jsonify,
    request,
    abort,
    make_response,
    redirect
)

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


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout():
    """Logout user by destroying the session.

    Returns:
       Response: A Flask Response with redirection or 403 status.
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)

    if user or session_id:
        # If a user exists, destroy the session and redirect to "/"
        AUTH.destroy_session(user.id)
        return redirect("/")
    else:
        # If no user is found, respond with a 403 Forbidden status
        abort(403)


@app.route("/profile", methods=["GET"], strict_slashes=False)
def profile():
    """Get user profile based on the session ID.

    Returns:
       Response: A Flask Response with JSON payload or 403 status.
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)

    if user:
        # If user exists, respond with status code 200 and user's email
        return jsonify({"email": user.email}), 200
    else:
        # If no user exists or invalid session ID, respond with 403 status
        abort(403)


@app.route("/reset_password", methods=["POST"], strict_slashes=False)
def get_reset_password_token():
    """Generate a reset password token based on the provided email.

    Returns:
       Response: A Flask Response with JSON payload or 403 status.
    """
    email = request.form.get("email")

    try:
        # Generate a reset password token for the specified email
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token}), 200

    except ValueError:
        # If user isn't found, abort with a 403 Forbidden status
        abort(403, {"message": "Forbidden"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
