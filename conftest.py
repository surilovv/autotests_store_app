from base.auth import Auth
from requests import Session
from env_config import Routes, Creds
from routers.stores import Stores
from pytest import fixture




########################
# App fixtures
########################


@fixture(scope='session')
def create_session():
    return Session()

@fixture(scope='session')
def get_token(create_session):
    auth = Auth(create_session, Routes.AUTH_URL, "admin", "bsdOneq1")
    auth.register()
    yield auth.generate_token()

@fixture()
def stores_route(create_session, get_token):
    yield Stores(create_session, Routes.STORE_URL, get_token)

