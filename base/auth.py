from requests import Session
from base.base_api import BaseAPI
from support.errors import TokenNotFound, TokenNotGranted


class Auth(BaseAPI):
    def __init__(self, session: Session, route: str, app_username: str, app_password: str):
        super().__init__(session, route)
        self.app_username = app_username
        self.app_password = app_password
        self.headers = {'accept': 'application/json', "Content-Type": "application/x-www-form-urlencoded"}

    def generate_token(self):
        response = self.post(f"{self.route}/token",
                             data={'username': self.app_username, 'password': self.app_password},
                             headers=self.headers)

        if response.status_code == 200:
            token = response.json().get('access_token')
            if token is None:
                raise TokenNotFound
            return token
        else:
            raise TokenNotGranted(response.status_code)
