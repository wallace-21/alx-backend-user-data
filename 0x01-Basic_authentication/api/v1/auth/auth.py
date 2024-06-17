#!/usr/bin/env python3

"""" import flask"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ class to manage the API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Define which routes don't need authentication
        """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        if not path.endswith("/"):
            path += "/"
        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """ returns None for requests
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ returns None cfor requests
        """
        return None
