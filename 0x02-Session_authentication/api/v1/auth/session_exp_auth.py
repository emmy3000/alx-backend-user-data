#!/usr/bin/env python3
"""
Custom API session authentication and expiration
assignment handler.
"""
import os
from datetime import datetime, timedelta
from api.v1.auth.session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """
    Sub-class of session authenitication providing
    supporting for assigning expiration dates.
    """

    def __init__(self):
        """
        Class instance constructor
        """
        try:
            duration = int(os.getenv('SESSION_DURATION'))
        except Exception:
            duration = 0

        self.session_duration = duration

    def create_session(self, user_id=None):
        """Method creates a Session ID for a user.

        Args:
          user_id (str): User ID for which the session is created.

        Returns:
          str: Session ID.
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        session_dictionary = {"user_id": user_id, "created_at": datetime.now()}
        self.user_id_by_session_id[session_id] = session_dictionary

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Method returns a user ID based on a session ID.

        Args:
            session_id (str): Session ID.

        Returns:
            str: User ID or None if session_id is None, not a string,
            or session is expired.
        """
        if session_id is None:
            return None

        user_details = self.user_id_by_session_id.get(session_id)
        if user_details is None or "created_at" not in user_details:
            return None

        created_at = user_details["created_at"]
        if self.session_duration > 0:
            allowed_window = created_at + \
                timedelta(seconds=self.session_duration)
            if allowed_window < datetime.now():
                return None

        return user_details.get("user_id")
