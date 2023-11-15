#!/usr/bin/env python3
""" UserSession module
"""
from models.base import Base


class UserSession(Base):
    """
    UserSession class represents a user session.

    Attributes:
        user_id (str): The user ID associated with the session.
        session_id (str): The unique identifier for the session.
    """

    def __init__(self, *args: list, **kwargs: dict):
        """
        Method initialize a UserSession's instance.

        Args:
            *args (list): Variable positional arguments.
            **kwargs (dict): Variable keyword arguments.
                user_id (str): The user ID associated with the session.
                session_id (str): The unique identifier for the session.
        """
        # Extract values from positional arguments if available
        if args:
            self.user_id = args[0]
            self.session_id = args[1] if len(args) > 1 else None
        else:
            # Extract values from keyword arguments
            self.user_id = kwargs.get('user_id')
            self.session_id = kwargs.get('session_id')
