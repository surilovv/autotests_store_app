import allure

from env_config import ExpectedData
def test_get_store(stores_route):
    stores_route.get_store(ExpectedData.STORE,1)

@allure.description("получение объекта магазин по id")
@allure.title("Get store")
@allure.label("owner", "Dima")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("E2E")
def test_1():
    with allure.step("step1"):
        assert 1 == 2
