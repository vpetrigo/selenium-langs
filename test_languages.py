from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")


def test_spanish_language(browser) -> None:
    expected = "Añadir al carrito"
    browser.get(link)
    actual = browser.find_element(*ADD_TO_CART_BUTTON).text
    assert actual == expected, f"{actual} != {expected} in Spanish language"


def test_french_language(browser) -> None:
    expected = "Ajouter au panier"
    browser.get(link)
    actual = browser.find_element(*ADD_TO_CART_BUTTON).text
    assert actual == expected, f"{actual} != {expected} in French language"
