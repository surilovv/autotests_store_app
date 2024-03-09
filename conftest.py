# from base.auth import Auth
# from requests import Session
# from base.db.models import Store, Product
# from env_config import Routes, PreparedData, Creds
# from routes.stores import Stores
# from pytest import fixture
# from base.db.database import Database
#
#
# ########################
# # Database fixtures
# ########################
#
#
# @fixture(autouse=True, scope="session")
# def database_operations():
#     # connection to Database
#     database = Database(
#         Creds.DATABASE_CONN_STRING
#     )
#
#     # prepare test dataset
#     dataset = [
#         Store(**PreparedData.STORE_1),
#         Store(**PreparedData.STORE_2),
#         Product(**PreparedData.PRODUCT_1)
#     ]
#     for data in dataset:
#         database.add(data)
#
#     print(dataset)
#
#     yield database.session
#
#     # cleanup DB
#     delete_data = [
#         (Store, {"store_id": 1}),
#         (Store, {"store_id": 2}),
#         (Product, {"product_name": "iphone"}),
#     ]
#     for table, condition in delete_data:
#         database.delete(table, **condition)
#
#     # disconnect
#     database.close()
#
# ########################
# # App fixtures
# ########################
#
#
# @fixture(scope='session')
# def create_session():
#     return Session()
#
# @fixture(scope='session')
# def get_token(create_session):
#     token = Auth(create_session, Routes.AUTH_URL, "admin", "bsdOneq1").generate_token()
#     yield token
#
# @fixture()
# def stores_route(create_session, get_token):
#     yield Stores(create_session, Routes.STORE_URL, get_token)
#
