import os
import pytest

from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver import ChromeOptions

options = None


def pytest_runtest_setup(item):
    global options

    language_to_use = "es" if item.function.__name__ == "test_spanish_language" else "fr"
    prefs = {
        "translate_whitelists": {"your native language": language_to_use},
        "translate": {"enabled": "True"},
        "intl.accept_languages": language_to_use
    }
    options = ChromeOptions()
    options.add_experimental_option("prefs", prefs)
    options.add_argument(f"--lang={language_to_use}")


@pytest.fixture
def browser() -> Remote:
    if os.getenv("TRAVIS") is not None:
        options.add_argument("--no-sandbox")
        options.add_argument("--headless")

    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
