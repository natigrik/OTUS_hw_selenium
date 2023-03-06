import pytest
import os

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser", choices=["chrome", "firefox", "opera", "edge", "ff", "ya"], default="chrome"
    )
    parser.addoption(
        "--driver_storage", default=os.path.expanduser("~/Devs/drivers")
    )
    parser.addoption(
        "--headless", action="store_true"
    )
    parser.addoption(
        "--maximized", action="store_true"
    )
    parser.addoption(
        "--url", default="https://demo.opencart.com/"
    )


@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption("--browser")
    driver_storage = request.config.getoption("--driver_storage")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")

    _driver = None

    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.headless = headless
        _driver = webdriver.Chrome(executable_path=f"{driver_storage}/chromedriver", options=chrome_options)

    elif browser_name == "firefox" or browser_name == "ff":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.headless = headless
        firefox_options.binary_location = "/usr/bin/firefox/firefox"
        _driver = webdriver.Firefox(executable_path=f"{driver_storage}/geckodriver.exe", options=firefox_options)

    elif browser_name == "edge":
        edge_options = webdriver.EdgeOptions()
        edge_options.headless = headless
        edge_options.binary_location = "/opt/microsoft/msedge-beta/msedge"
        _driver = webdriver.Edge(executable_path=f"{driver_storage}/msedgedriver", options=edge_options)

    elif browser_name == "yandex" or browser_name == "ya":
        yandex_options = webdriver.ChromeOptions()
        yandex_options.headless = headless
        _driver = webdriver.Chrome(executable_path=f"{driver_storage}/yandexdriver.exe", options=yandex_options)

    if maximized:
        _driver.maximize_window()

    yield _driver

    _driver.quit()


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")
