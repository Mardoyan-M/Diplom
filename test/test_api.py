import requests
import allure

url = "https://api.kinopoisk.dev/v1.4/movie"
headers = {
    "Content-Type": "application/json",
    "x-api-key": "404S4VY-715MFQM-NBQGYPF-H83YJPH"
}


@allure.title("Позитивный тест: поиск по id")
@allure.description("Тест проверяет успешный поиск фильма по id.")
@allure.feature("Поиск фильмов")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_by_id():
    with allure.step("Отправка запроса для поиска фильма по id"):
        response = requests.request("GET", f"{url}/{44168}", headers=headers)
    with allure.step("Проверка статус-кода ответа"):
        assert response.status_code == 200


@allure.title("Позитивный тест: поиск по названию")
@allure.description("Тест проверяет успешный поиск фильма по названию.")
@allure.feature("Поиск фильмов")
@allure.severity(allure.severity_level.NORMAL)
def test_search_by_name():
    params = {
        "page": 1,
        "limit": 10,
        "query": "The Girls"
    }
    with allure.step("Отправка запроса для поиска фильма по названию"):
        response = requests.request("GET", url, params=params, headers=headers)
    with allure.step("Проверка статус-кода ответа"):
        assert response.status_code == 200


@allure.title("Позитивный тест: получение списка жанров")
@allure.description("Тест проверяет получение списка жанров фильмов.")
@allure.feature("Получение жанров")
@allure.severity(allure.severity_level.NORMAL)
def test_list_of_genres():
    params = {
        "field": "genres.name"
    }
    with allure.step("Отправка запроса для получения списка жанров"):
        response = requests.request("GET", url, params=params, headers=headers)
    with allure.step("Проверка статус-кода ответа"):
        assert response.status_code == 200


@allure.title("Негативный тест: Поиск по id со значением менее 250")
@allure.description("Тест проверяет ответ сервера при поиске по id < 250.")
@allure.feature("Поиск фильмов")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_by_id_1():
    with allure.step("Отправка запроса для поиска фильма по id < 250"):
        response = requests.request("GET", f"{url}/{249}", headers=headers)
    with allure.step("Проверка статус-кода ответа на ошибку"):
        assert response.status_code == 400


@allure.title("Негативный тест: Поиск по id со значением более 7000000")
@allure.description("Тест проверяет ответ сервера при поиске по id > 7000000.")
@allure.feature("Поиск фильмов")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_by_id_2():
    with allure.step("Отправка запроса для поиска фильма по id > 7000000"):
        response = requests.request("GET", f"{url}/{7000001}", headers=headers)
    with allure.step("Проверка статус-кода ответа на ошибку"):
        assert response.status_code == 400
