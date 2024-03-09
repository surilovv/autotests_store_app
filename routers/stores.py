from base.base_api import BaseAPI
from requests import Session
from support.assertions import Assertions


class Stores(BaseAPI):

    def __init__(self, session: Session, route: str, token: str):
        super().__init__(session, route)
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "applications/json"
        }

    def create_store(self, payload, expected_data):
        response = self.post(url=f"{self.route}/create_store",
                             headers=self.headers,
                             json=payload)
        Assertions.assert_equal(response.status_code, 200)
        Assertions.assert_equal(response.json(), expected_data)

    def get_stores(self, expected_data):
        response = self.get(url=f"{self.route}/get-stores",
                            headers=self.headers)
        Assertions.assert_equal(response.status_code, 200)
        Assertions.assert_equal(response.json(), expected_data)

    def get_store(self, expected_data, path_param):
        response = self.get(url=f"{self.route}/get-store/{path_param}",
                            headers=self.headers)
        Assertions.assert_equal(response.status_code, 200)
        Assertions.assert_equal(response.json(), expected_data)