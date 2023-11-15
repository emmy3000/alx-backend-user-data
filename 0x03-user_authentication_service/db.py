#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import NoResultFound, InvalidRequestError
from sqlalchemy.orm.exc import MultipleResultsFound

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database

        Args:
            email (str): User's email
            hashed_password (str): Hashed password for the user

        Returns:
            User: The created User object
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """Find a user by given filter criteria.

        Args:
            **kwargs: Arbitrary keyword arguments representing
            filter criteria.

        Returns:
            User: The found User object.

        Raises:
            NoResultFound: If no result is found.
            InvalidRequestError: If an invalid query argument is provided.
            MultipleResultsFound: If multiple results are found.
        """
        try:
            user = self._session.query(User).filter_by(**kwargs).one()
            return user
        except NoResultFound as e:
            raise e
        except (InvalidRequestError, MultipleResultsFound) as e:
            raise InvalidRequestError("Invalid query argument") from e
