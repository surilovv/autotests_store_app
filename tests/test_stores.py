from env_config import ExpectedData
def test_get_store(stores_route):
    stores_route.get_store(ExpectedData.STORE,1)