from dotenv import load_dotenv
import os
from support.json_handler import JSONHandler


class Creds:
    load_dotenv()


    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DATABASE_CONN_STRING = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
class Routes:
    BASE_URL = "http://172.17.0.1:8080"
    STORE_URL = f"{BASE_URL}/store"
    PRODUCT_URL = f"{BASE_URL}/product"
    AUTH_URL = f"{BASE_URL}/auth"

class ConfigPath:
    ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
    EXPECTED_DATA = os.path.join(ROOT_DIR, "data", "expected_data.json")


class ExpectedData:
    STORES = JSONHandler.load_json(ConfigPath.EXPECTED_DATA)
    STORE = JSONHandler.load_json(ConfigPath.EXPECTED_DATA)[0]




