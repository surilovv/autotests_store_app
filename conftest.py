from base.auth import Auth
from requests import Session
from base.db.models import Store, Product
from env_config import Routes, PreparedData, Creds
from routers.stores import Stores
from pytest import fixture
from base.db.database import Database



########################
# App fixtures
########################


@fixture(scope='session')
def create_session():
    return Session()

@fixture(scope='session')
def get_token(create_session):
    token = Auth(create_session, Routes.AUTH_URL, "admin", "bsdOneq1").generate_token()
    yield token

@fixture()
def stores_route(create_session, get_token):
    yield Stores(create_session, Routes.STORE_URL, get_token)

