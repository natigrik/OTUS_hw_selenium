from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def assert_visibility_element(selector, driver, timeout=1, by=By.CSS_SELECTOR):
    try:
        return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, selector)))
    except TimeoutException:
        raise AssertionError(f"Не найден элемент: {selector}")


def assert_clickable_element(selector, driver, timeout=1, by=By.CSS_SELECTOR):
    try:
        return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, selector)))
    except TimeoutException:
        raise AssertionError(f"Не найден элемент: {selector}")


def test_main_page(driver, base_url):
    driver.get(base_url)
    element = assert_visibility_element("#logo", driver)
    element = assert_clickable_element("div#search input[name=search]", driver)
    element = assert_clickable_element("div#header-cart button[data-bs-toggle=dropdown]", driver)
    element = assert_visibility_element("#menu", driver)
    element = assert_visibility_element("div.carousel-inner", driver)
    element = assert_visibility_element("div.product-thumb", driver)
    element = assert_clickable_element(".product-thumb .image", driver)


def test_catalog_desktop_page(driver, base_url):
    driver.get(f"{base_url}/index.php?route=product/category&path=20")
    element = assert_visibility_element("#logo", driver)
    element = assert_clickable_element("div#search input[name=search]", driver)
    element = assert_clickable_element("div#header-cart button[data-bs-toggle=dropdown]", driver)
    element = assert_visibility_element(".breadcrumb", driver)
    element = assert_clickable_element("#column-left", driver)
    element = assert_clickable_element("#carousel-banner-0", driver)
    element = assert_visibility_element("h2", driver)
    element = assert_clickable_element("#column-left", driver)
    element = assert_clickable_element("a#compare-total", driver)
    element = assert_clickable_element("select#input-sort", driver)
    element = assert_clickable_element("select#input-limit", driver)
    element = assert_visibility_element("#product-list", driver)
    element = assert_visibility_element(".text-start", driver)
    element = assert_visibility_element(".text-end", driver)


def test_tablet_item_page(driver, base_url):
    driver.get(f"{base_url}/index.php?route=product/product&path=57&product_id=49")
    element = assert_visibility_element(".breadcrumb", driver)
    element = assert_clickable_element("img.img-thumbnail", driver)
    element = assert_visibility_element(".price-new", driver)
    element = assert_clickable_element("button[data-bs-original-title='Add to Wish List']", driver)
    element = assert_clickable_element("button[data-bs-original-title='Compare this Product']", driver)
    element = assert_clickable_element("input[name=quantity]", driver)
    element = assert_clickable_element("button#button-cart", driver)


def test_login_admin_page(driver, base_url):
    driver.get(f"{base_url}/admin/")
    element = assert_visibility_element(".card-header", driver)
    element = assert_visibility_element("label[for=input-username]", driver)
    element = assert_clickable_element("#input-username", driver)
    element = assert_visibility_element("label[for=input-password]", driver)
    element = assert_clickable_element("#input-password", driver)
    element = assert_clickable_element("button[type = submit]", driver)


def test_register_page(driver, base_url):
    driver.get(f"{base_url}/index.php?route=account/register")
    element = assert_visibility_element("#logo", driver)
    element = assert_clickable_element("div#search input[name=search]", driver)
    element = assert_clickable_element("div#header-cart button[data-bs-toggle=dropdown]", driver)
    element = assert_visibility_element(".breadcrumb", driver)
    element = assert_visibility_element("h1", driver)
    element = assert_clickable_element("fieldset#account input#input-firstname", driver)
    element = assert_clickable_element("fieldset#account input#input-lastname", driver)
    element = assert_clickable_element("fieldset#account input#input-email", driver)
    element = assert_clickable_element("fieldset input#input-password", driver)
    element = assert_clickable_element("input[type=checkbox][name=agree]", driver)
    element = assert_clickable_element("button[type=submit]", driver)
