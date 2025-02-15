import os
from dotenv import load_dotenv
import requests
from django.conf import settings
from django.contrib.sessions.models import Session
from django.core.exceptions import ObjectDoesNotExist


load_dotenv()

class AuthBusiness:
    __email = None
    __password = None
    __auth_url = None
    def __init__(self):
        self.__email = os.getenv("EMAIL") or None
        self.__password = os.getenv("PASSWORD") or None
        self.__auth_url = (str(os.getenv("AUTH_PROVIDER_URL")) + "/auth") or None

    def authenticate(self, request):
        email = request.data.get("email") or self.__get_email()
        password = request.data.get("password") or self.__get_password()
        if not email or not password:
            raise Exception("Email or password is missing")
        data = {
            "email": email,
            "password": password
        }
        response = requests.post(self.__get_auth_url(), json=data)
        if response.status_code != 200:
            raise Exception(f"Authentication failed with status code {response.status_code}")
        print("response: ")
        response_data = response.json()
        token = response_data.get("token")
        if not token:
            raise Exception("Token not found in the response")
        self.__save_session_token(request, token)
        return response_data
    
    def __save_session_token(self, request, token):
        request.session['auth_token'] = token
    
    def __get_email(self):
        return self.__email

    def __get_password(self):
        return self.__password
    
    def __get_auth_url(self):
        return self.__auth_url
