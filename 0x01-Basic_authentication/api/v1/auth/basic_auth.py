#!/usr/bin/env python3
"""
Custom basic API authentication
"""
from api.v1.auth.auth import Auth
import base64
import binascii


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
