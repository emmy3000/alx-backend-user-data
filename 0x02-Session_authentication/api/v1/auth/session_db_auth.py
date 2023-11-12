#!/usr/bin/env python3
"""
Custom API session authentication providing
expiration and storage support.
"""
from flask import request
from datetime import datetime, timedelta
from models.user_session import UserSession
from api.v1.auth.session_exp_auth import SessionExpAuth


class SessionDBAuth(SessionExpAuth):
    """Sub-class of the session authentication responsible
    for expiration and storage management.
    """

    def create_session(self, user_id=None) -> str:
        """Method creates and stores a session ID
        for the user.

        Args:
          user_id: User ID for which the session is created.

        Returns:
          str: The generated session ID.

        Notes:
          The session ID is also stored in the database.
        """
        session_id = super().create_session(user_id)
        if if isinstance(session_id, str):
            kwargs = {'user_id': user_id, 'session_id': session_id}
            user_session = UserSession(**kwargs)
            user_session.save()

            return session_id

    def user_id_for_session_id(self, session_id=None):
        """Method retrieves the user ID associated
        with a given session ID.

        Args:
          session_id: Session ID to retrieve the user ID for.

        Returns:
          str: The user ID associated with the session ID, or
          None if not found or if the session has expired.
        """
        try:
            sessions = UserSession.search({'session_id': session_id})
        except Exception:
            return None

        if not sessions:
            return None

        cur_time = datetime.now()
        session = sessions[0]
        expiration_time = session.created_at + \
            timedelta(seconds=self.session_duration)

        if expiration_time < current_time:
            return None

        return session.user_id

    def destroy_session(self, request=None) -> bool:
        """Method destroys an authenticated session.

        Args:
          request: Flask request object containing the session cookie.

        Returns:
          bool: True if the session is successfully destroyed,
          False otherwise.
        """
        session_id = self.session_cookie(request)

        try:
            sessions = UserSession.search({'session_id': session_id})
        except Exception:
            return False

        if not sessions:
            return False

        sessions[0].remove()
        return True
