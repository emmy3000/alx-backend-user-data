#!/usr/bin/env python3
"""
Authentication module.
"""
import bcrypt
import uuid
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Generate a salted hash of the input password.

    Args:
        password (str): The input password.

    Returns:
        bytes: Salted hash of the input password.
    """
    # Generate a random salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password


def _generate_uuid() -> str:
    """Generate a string representation of a new UUID.

    Returns:
        str: A string representation of a new UUID.
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Initialize a new Auth instance.

        The constructor creates a new instance of the Auth class
        used for interacting with the authentication database.

        Attributes:
            _db (DB): An instance of the DB class for database
            interactions.
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user.

        Args:
            email (str): The user's email.
            password (str): The user's password.

        Returns:
            User: The newly created User object.

        Raises:
            ValueError: If a user with the given email
            already exists.
        """
        try:
            # Check if user with the given email already exists
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))

        except NoResultFound:
            # User doesn't exist, proceed with registration
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """Validate the user's login credentials.

        Args:
            email (str): The user's email.
            password (str): The user's password.

        Returns:
            bool: True if the login credentials are valid,
            and False otherwise.
        """
        try:
            # Check if a specified email exists in the database
            user = self._db.find_user_by(email=email)
            hashed_password = user.hashed_password
            passwd = password.encode("utf-8")
            return bcrypt.checkpw(passwd, hashed_password)

        except NoResultFound:
            # Return False if no user is found with the specified email
            return False

        except Exception as e:
            # Handle other exceptions gracefully
            print("An error occurred: {}".format(e))
            return False

    def create_session(self, email: str) -> str:
        """Create a new session for the user with the specified email.

        Args:
           email (str): The user's email.

        Returns:
           str: The session ID.
        """
        try:
            # Find the user by email and create a new session ID
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            user.session_id = session_id
            self._db._session.commit()
            return session_id

        except NoResultFound:
            # Return None if no user is found with the specified email
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """Get a user based on the provided session ID.

        Args:
           session_id (str): The session ID.

        Returns:
           User: The corresponding User object or None if not found.
        """
        # Check if the session ID is None; if so, return None
        if session_id is None:
            return None

        try:
            # Attempt to find a user with the provided session ID
            user = self._db.find_user_by(session_id=session_id)
            return user

        except NoResultFound:
            # Return None if no user exists with the provided session ID
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroys the session of the user with the specified user ID.

        Args:
           user_id (int): The user's ID.

        Returns:
           Updates the user's session ID to None if the user exists,
           or does nothing otherwise.
        """
        try:
            # Find the user by user ID and update the session ID to None
            user = self._db.find_user_by(id=user_id)
            user.session_id = None
            self._db._session.commit()

        except NoResultFound:
            # No user found with the specified user ID
            pass

    def get_reset_password_token(self, email: str) -> str:
        """Get the reset password token for the user
        with the given email.

        Args:
           email (str): The email of the user.

        Returns:
           str: The reset password token.

        Raises:
           ValueError: If the user does not exist.
        """
        user = self._get_user_by_email(email)

        if not user:
            raise ValueError("User with email {} not found.".format(email))

        reset_token = _generate_uuid()
        self._db.update_user(user.id, reset_token=reset_token)

        return reset_token
