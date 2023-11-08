#!/usr/bin/env python3
"""
API authentication management
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """Auth class to manage API authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for a given path
        Args:
          @params:path (str): The path to check for authentication.
          @params:excluded_paths (List[str]): List of excluded paths.
        Return:
          bool: True if authentication is required, False if not.
        """
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        path = path if path.endswith('/') else path + '/'
        return not any(path.startswith(excluded)
                       for excluded in excluded_paths)

    def authorization_header(self, request=None) -> str:
        """Get the authorization header from the request.
        Args:
          @params:request (Request): The Flask request object.
        Return:
          str: The authorization header value, or None if not found.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Get the current user based on the request.
        Args:
          @params:request (Request): The Flask request object.
        Return:
          TypeVar('User'): The current user, or None if not available.
        """
        return None
