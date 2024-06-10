#!/usr/bin/python3

"""" import flask"""
from flask import request


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ returns False for path
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ returns None for requests
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ returns None cfor requests
        """
        return None
