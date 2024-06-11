#!/usr/bin/env python3

"""Import the necessary imports"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    """Create a user table
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=False)
    reset_token = Column(String(250), nullable=False)

    def __repr__(self):
        """ format"""
        return ("{}\n{}\n{}\n{}\n{}".format(self.id, self.email,
                self.hashed_password, self.session_id, self.reset_token))
