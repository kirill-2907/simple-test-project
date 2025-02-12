from playwright.sync_api import Page, Locator

from pages.simple_button_page import SimpleButtonPage


class MainPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def click_link_simple_button(self) -> SimpleButtonPage:
        self.simple_button.click()
        return SimpleButtonPage(self.page)

    @property
    def simple_button(self) -> Locator:
        return self.page.get_by_role('link', name='Simple button')
