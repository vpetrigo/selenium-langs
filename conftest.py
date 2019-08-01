import pytest

from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver import ChromeOptions

options = None


def pytest_runtest_setup(item):
    global options

    language_to_use = "es" if item.function.__name__ == "test_spanish_language" else "fr"
    options = ChromeOptions()
    options.add_argument(f"--lang={language_to_use}")


@pytest.fixture
def browser() -> Remote:
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
