#!/usr/bin/env python3
"""
This module demonstrates password encryption using bcrypt.

Bcrypt is a strong and secure password hashing algorithm
that helps protect user passwords.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password with a randomly generated salt.

    Args:
        password (str): The password to be hashed.

    Returns:
        bytes: The salted and hashed password.
    """
    if password is not None and isinstance(password, str):
        return bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates a password by comparing it to a hashed password.

    Args:
        hashed_password (bytes): The previously hashed password.
        password (str): The password to be validated.

    Returns:
        bool: True if the password is valid, False otherwise.
    """
    if isinstance(hashed_password, bytes) and isinstance(password, str):
        return bcrypt.checkpw(bytes(password, 'utf-8'), hashed_password)
    return False


if __name__ == '__main__':
    """
    Tests the functionality of the password hashing and validation.
    """
    pwd = 'This is some text'
    print('Password: [{}]\nHashed Password: {}'.format(pwd, hash_password(pwd)))
    print('Is Valid: {}\n'.format(is_valid(hash_password(pwd), pwd))

    pwd = '1 l0v3 7h3 w1ld!'
    print('Password: [{}]\nHashed Password: {}'.format(pwd, hash_password(pwd)))
    print('Is Valid: {}\n'.format(is_valid(hash_password(pwd), pwd))

    pwd = ''
    print('Password: [{}]\nHashed Password: {}'.format(pwd, hash_password(pwd)))
    print('Is Valid: {}\n'.format(is_valid(hash_password(pwd), pwd))

    pwd = '2'
    print('Password: [{}]\nHashed Password: {}'.format(pwd, hash_password(pwd)))
    print('Is Valid: {}'.format(is_valid(hash_password(pwd), pwd))
