#!/usr/bin/env python3
"""
Custom API authentication
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """Auth class managing API authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if authentication is required for a given path.

        Args:
            path (str): The path to check for authentication.
            excluded_paths (List[str]): List of excluded paths.

        Return:
            bool: True if authentication is required, False if not.
        """
        if path is None or excluded_paths is None or not excluded_paths:
            return True

        for excluded_path in excluded_paths:
            if excluded_path.endswith("*") and path.startswith(excluded_path[:-1]):
                return False
            elif path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Get the authorization header from the request.

        Args:
          request (Request): The Flask request object.

        Return:
          str: The authorization header value, or None if not found.
        """
        if not request or not request.headers or not request.headers.get(
                'Authorization'):
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Get the current user based on the request.

        Args:
          request (Request): The Flask request object.

        Return:
          TypeVar('User'): The current user, or None if not available.
        """
        return None
