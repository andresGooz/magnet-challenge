import os
import requests
from django.conf import settings
from django.contrib.sessions.models import Session
from django.core.exceptions import ObjectDoesNotExist


class AuthBusiness:
    __email = None
    __password = None
    __auth_url = None
    def __init__(self):
        self.__email = os.getenv("EMAIL")
        self.__password = os.getenv("PASSWORD")
        self.__auth_url = os.getenv("AUTH_PROVIDER_URL") + "/auth"
        if not self.__email or not self.__password:
            raise Exception("Email or password is missing")

    @staticmethod
    def authenticate(self, email = None, password = None):
        data = {
            "email": email or self.__get_email(self),
            "password": password or self.__get_password(self)
        }
        response = requests.post(self.__get_auth_url(), json=data)
        if response.status_code != 200:
            raise Exception(f"Authentication failed with status code {response.status_code}")
        response_data = response.json()
        token = response_data.get("token")
        if not token:
            raise Exception("Token not found in the response")
        self.__save_session_token(token)
        return response_data
    
    def __save_session_token(self, token):
        requests.session['auth_token'] = token
    
    def __get_email(self):
        return self.__email

    def __get_password(self):
        return self.__password
    
    def __get_auth_url(self):
        return self.__auth_url
