import os
import tempfile
import pytest

from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver import ChromeOptions

options = None


def pytest_runtest_setup(item):
    global options

    language_to_use = (
        "es-ES" if item.function.__name__ == "test_spanish_language" else "fr-FR"
    )
    options = ChromeOptions()
    options.add_argument(f"--lang={language_to_use}")


@pytest.fixture
def browser() -> Remote:
    if os.getenv("TRAVIS") is not None or os.getenv("GITHUB_WORKFLOW") is not None:
        options.add_argument("--no-sandbox")
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")

    with tempfile.TemporaryDirectory() as tmp:
        options.add_argument(f"--user-data-dir={tmp}")
        browser = webdriver.Chrome(options=options)
        yield browser
        browser.quit()
