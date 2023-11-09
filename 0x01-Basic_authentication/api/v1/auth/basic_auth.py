#!/usr/bin/env python3
"""
Custom basic API authentication
"""
from api.v1.auth.auth import Auth


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
