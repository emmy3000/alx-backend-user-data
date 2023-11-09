#!/usr/bin/env python3
"""
Custom basic API authentication
"""
from api.v1.auth.auth import Auth
import base64
import binascii
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """BasicAuth class for basic authentication management.
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """"Extract the Base64 part of the Authorization header
        for Basic Authentication.

        Args:
          authorization_header (str): The Authorization header.

        Return:
          str: The Base64 part of the Authorization header, or
          None if not found or invalid.
        """
        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None

        auth_parts = authorization_header.split()

        if len(auth_parts) != 2 or auth_parts[0] != "Basic":
            return None

        return auth_parts[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """"Decode a Base64 authorization header.

        Args:
          base64_authorization_header (str): The Base64 authorization header
          to decode.

        Return:
          str: The decoded value as a UTF-8 string.

        If the input is None or not a valid string or not valid Base64,
        it returns None.
        """
        if base64_authorization_header is None or not isinstance(
                base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_str = decoded_bytes.decode('utf-8')
            return decoded_str
        except binascii.Error:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Extract user email and password from a Base64 decoded header value.

        Args:
          decoded_base64_authorization_header (str): The decoded Base64 header
          value.

        Return:
          (str, str): A tuple containing the user email and password.
                      (None, None) if the input is invalid or doesn't
                      contain a ':'.
        """
        if decoded_base64_authorization_header is None or not isinstance(
                decoded_base64_authorization_header, str):
            return (None, None)

        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        user_email, user_password = decoded_base64_authorization_header.split(
            ':', 1)
        return user_email, user_password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Get the User instance based on email and password.
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        user_list = User.search({'email': user_email})

        if not user_list:
            return None

        user = user_list[0]

        if not user.is_valid_password(user_pwd):
            return None

        return user
