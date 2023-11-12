#!/usr/bin/env python3
"""
Custom API session authentication management
"""
import base64
from uuid import uuid4
from typing import Union, TypeVar
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """ Class for handling Session Authorization protocols.
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a session ID for a user with the given user_id.

        Args:
            user_id (str): User's ID.

        Return:
            None if user_id is None or not a string.
            Session ID in string format.
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns a user ID associated with a given session ID.

        Args:
            session_id (str): Session ID

        Return:
            user id or None if session_id is None or not a string
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Return a user instance based on a cookie value.

        Args:
            request: Request object containing cookie.

        Returns:
            User instance
        """
        session_cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_cookie)
        user = User.get(user_id)

        return user

    def destroy_session(self, request=None):
        """Deletes a user session.

        Args:
          request: Request object.

        Returns:
          bool: True if the session was successfully deleted,
          False otherwise.
        """
        if request is None:
            return False

        session_cookie = self.session_cookie(request)
        if session_cookie is None:
            return False

        user_id = self.user_id_for_session_id(session_cookie)
        if user_id is None:
            return False

        del self.user_id_by_session_id[session_cookie]
        return True
