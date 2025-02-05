import pytest
import allure
from pages.main_page import MainPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import main_url, cookies


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument(
        "--disable-blink-features=AutomationControlled")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome()

    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    driver.get(main_url)

    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.get(main_url)
    return MainPage(driver, main_url)


@allure.feature("Smoke")
@allure.story("UI")
@allure.title("Проверка заголовка главной страницы")
@pytest.mark.smoke
def test_check_main_page_title(main_page):
    with allure.step("Заголовок главной страницы"):
        assert main_page.check_page_title(
            "Кинопоиск. Онлайн кинотеатр. Фильмы сериалы мультфильмы и энциклопедия")


@allure.feature("Поиск")
@allure.story("UI")
@allure.title("Поиск фильмов по названию")
@pytest.mark.parametrize("film_title",
                         ["Девчата", "Титаник"])
def test_search_book_by_title(main_page, film_title):
    with allure.step(f"Поиск фильмов по названию"
                     f" {film_title}"):
        main_page.search_items_by_phrase(film_title)
    with allure.step("Количество результатов больше 0"):
        assert main_page.get_search_results_count() > 0
    with allure.step("Название фильма содержится в результатах"):
        assert film_title in main_page.find_book_titles()


@allure.feature("Навигация")
@allure.story("UI")
@allure.title("Проверка навигации к разделу 'Сериалы'")
@pytest.mark.ui
def test_navigate_to_series_section(main_page):
    with allure.step("Навигация к разделу 'Сериалы'"):
        series_link = main_page.get_series_link()
        series_link.click()


@allure.feature("Навигация")
@allure.story("UI")
@allure.title("Проверка навигации к разделу 'Фильмы'")
@pytest.mark.ui
def test_navigate_to_cinema_section(main_page):
    with allure.step("Навигация к разделу 'Фильмы'"):
        cinema_link = main_page.get_cinema_link()
        cinema_link.click()


@allure.feature("Навигация")
@allure.story("UI")
@allure.title("Проверка навигации к разделу 'Спорт'")
@pytest.mark.ui
def test_navigate_to_sport_section(main_page):
    with allure.step("Навигация к разделу 'Спорт'"):
        sport_link = main_page.get_sport_link()
        sport_link.click()
