#!/usr/bin/env python3
""" Basic Authentication Implementation """

from typing import TypeVar
from models.user import User
from base64 import b64decode
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth class """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Return Base64 part of Authorization header """
        if authorization_header is None or not isinstance(authorization_header,
                                                          str) \
                or not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Return decoded value of Base64 string """
        if base64_authorization_header is None or not isinstance(
                base64_authorization_header, str):
            return None
        try:
            return b64decode(base64_authorization_header).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ Returns user email and password from decoded value """
        if decoded_base64_authorization_header is None or not isinstance(
                decoded_base64_authorization_header, str) \
                or decoded_base64_authorization_header.find(':') == -1:
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """ Returns the user instance based on his email and password """
        if user_email is None or not isinstance(user_email, str) \
                or user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            user = User.search({'email': user_email})
        except Exception:
            return None
        for u in user:
            if u.is_valid_password(user_pwd):
                return u
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Overloads Auth and retrieves the User instance for a request """
        if request is None:
            return None
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None
        b64_auth_header = self.extract_base64_authorization_header(
            auth_header)
        if b64_auth_header is None:
            return None
        decoded_auth_header = self.decode_base64_authorization_header(
            b64_auth_header)
        if decoded_auth_header is None:
            return None
        user_credentials = self.extract_user_credentials(decoded_auth_header)
        if user_credentials is None:
            return None
        user = self.user_object_from_credentials(user_credentials[0],
                                                 user_credentials[1])
        return user
