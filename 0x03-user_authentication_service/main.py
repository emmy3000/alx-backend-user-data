#!/usr/bin/env python3
"""
Main module for running tests.
"""
import requests

BASE_URL = "http://localhost:5000"


def register_user(email: str, password: str) -> None:
    """Register a new user with the provided email
    and password.

    Args:
        email (str): Email address of the user to be registered.
        password (str): Password for the user account.

    Raises:
        AssertionError: If the registration request fails
        or returns an unexpected response.

    Returns:
        None
    """
    # Make a POST request to register the user
    response = requests.post(
        "{}/users".format(BASE_URL),
        data={
            "email": email,
            "password": password
        }
    )

    # Check the response status code and JSON content
    assert response.status_code in {200, 400}, \
        "Unexpected status code: {}".format(response.status_code)

    if response.status_code == 200:
        assert response.json() == {"email": email, "message": "user created"}
    else:
        assert response.json() == {"message": "email already registered"}, \
            "Unexpected JSON response: {}".format(response.json())


def log_in_wrong_password(email: str, password: str) -> None:
    """Attempt to log in with the provided email
    and incorrect password.

    Args:
        email (str): The email address of the user.
        password (str): The incorrect password for the user account.

    Raises:
        AssertionError: If the login request does not return a 401 status code,
        indicating unauthorized access.
    """
    login_url = "{}/sessions".format(BASE_URL)

    # Make a POST request to attempt login with the incorrect password
    response = requests.post(
        login_url,
        data={
            "email": email,
            "password": password
        }
    )

    # Check if the response status code is 401 (Unauthorized)
    assert response.status_code == 401, \
        "Unexpected status code: {}. \
            Expected 401 Unauthorized.".format(response.status_code)


def log_in(email: str, password: str) -> str:
    """Log in a user with the provided email and password.

    Args:
        email (str): The email address of the user.
        password (str): The password for the user account.

    Returns:
        str: The session ID obtained after successful login.

    Raises:
        AssertionError: If the login request doen't return a 200 status code,
        or if the response structure is unexpected.
    """
    # Make a POST request to log in the user
    response = requests.post(
        "{}/sessions".format(BASE_URL),
        data={
            "email": email,
            "password": password
        }
    )

    # Check the response status code and JSON content
    assert response.status_code == 200, \
        "Unexpected status code: {}".format(response.status_code)

    try:
        json_response = response.json()
        assert json_response == {"email": email, "message": "logged in"}, \
            "Unexpected JSON response: {}".format(json_response)

    except ValueError:
        assert False, "Invalid JSON response: {}".format(response.text)

    # Return the session ID obtained from the response cookies
    return response.cookies['session_id']


def profile_unlogged() -> None:
    """Test accessing the user profile without being
    logged in.

    Raises:
        AssertionError: If the request to access the profile doesn't return
        a 403 status code, indicating that the user isn't logged in.
    """
    # Make a GET request to access the profile without being logged in
    response = requests.get("{}/profile".format(BASE_URL))

    # Check the response status code
    assert response.status_code == 403, \
        "Unexpected status code: {}".format(response.status_code)


def profile_logged(session_id: str) -> None:
    """Test accessing the user profile when logged in.

    Args:
        session_id (str): The session ID of the logged-in user.

    Raises:
        AssertionError: If the request to access the profile doesn't return
        a 200 status code, indicating successful access to the user's profile.
    """
    # Set the cookies with the provided session ID
    cookies = {"session_id": session_id}

    # Make a GET request to access the user profile when logged in
    response = requests.get("{}/profile".format(BASE_URL), cookies=cookies)

    # Check the response status code
    assert response.status_code == 200, \
        "Unexpected status code: {}".format(response.status_code)


def log_out(session_id: str) -> None:
    """Test logging out a user with the provided session ID.

    Args:
        session_id (str): The session ID of the user to be logged out.

    Raises:
        AssertionError: If the request to log out the user does not return
        a 200 status code, indicating successful logout.
    """
    # Set the cookies with the provided session ID
    cookies = {"session_id": session_id}

    # Make a DELETE request to log out the user
    response = requests.delete("{}/profile".format(BASE_URL), cookies=cookies)

    # Check the response status code
    assert response.status_code == 200, \
        "Unexpected status code: {}".format(response.status_code)


def reset_password_token(email: str) -> str:
    """Test the generation of a reset password token for a user
    with the provided email.

    Args:
        email (str): The email address of the user for whom
        to generate a reset token.

    Returns:
        str: The reset token generated for the user.

    Raises:
        AssertionError: If the request to generate a reset token
        doesn't return a 200 status code or if the expected JSON
        payload is not received.
    """
    # Make a POST request to generate a reset token
    response = requests.post(
        "{}/profile".format(BASE_URL),
        data={"email": email}
    )

    # Check if the response status code is 200 or 401
    assert response.status_code in {200, 401}, \
        "Unexpected status code: {}".format(response.status_code)

    if response.status_code == 200:
        # Extract and return the reset token from the JSON payload
        return response.json()["reset_token"]
    else:
        # Check for an "Unauthorized" application
        assert response.status_code == 401, \
            "Unexpected status code: {}".format(response.status_code)


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Test the update of a user's password using a reset token.

    Args:
        email (str): The email address of the user.
        reset_token (str): The reset token associated with the user.
        new_password (str): The new password to set for the user.

    Raises:
        AssertionError: If the request to update the password does not return
        a 200 status code.
    """
    response = requests.put(
        f"{BASE_URL}/reset_password",
        data={
            "email": email,
            "reset_token": reset_token,
            "new_password": new_password
        }
    )

    if response.status_code == 200:
        expected_response = {
            "email": email,
            "message": "Password updated"
        }
        assert response.json() == expected_response, \
            "Unexpected JSON response: {}".format(response.json())
    else:
        assert response.status_code == 403, \
            "Unexpected status code: {}".format(response.status_code)


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
