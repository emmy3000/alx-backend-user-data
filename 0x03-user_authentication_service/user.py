#!/usr/bin/env python3
"""
Defines the User model for the 'users' table.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """SQLAlchemy model for the 'users' table.

    Attributes:
      id (int): The integer primary key.
      email (str): The non-nullable string representing the user's email.
      hashed_password (str): The non-nullable string representing
                             the hashed user password.
      session_id (str): The nullable string representing the user's session ID.
      reset_token (str): The nullable string representing the reset token
                         for password recovery.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
