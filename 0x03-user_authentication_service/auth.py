#!/usr/bin/env python3
"""
Generate a salted hash of the input password using bcrypt.
"""
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
