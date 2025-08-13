import pytest
from playwright.sync_api import sync_playwright, BrowserContext
from pages.main_page import MainPage


@pytest.fixture()
def f_browser() -> BrowserContext:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()


@pytest.fixture(autouse=True)
def f_main_page(f_browser: BrowserContext) -> None:
    page = f_browser.new_page()
    page.goto('https://www.qa-practice.com/')
    yield MainPage(page)
