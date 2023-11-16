#!/usr/bin/env python3
"""
Authentication module.
"""
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User
import bcrypt


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
