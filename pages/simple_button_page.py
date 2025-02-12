from playwright.sync_api import Locator, expect

from pages.base_page import BasePage
from pages.like_button_page import LikeButtonPage


class SimpleButtonPage(BasePage):

    def click_tab_like_button(self) -> LikeButtonPage:
        self.tab_like_button.click()
        return LikeButtonPage(self.page)

    def click_button_click(self) -> None:
        self.button_click.click()

    def check_button_click_is_visible(self) -> None:
        expect(self.button_click).to_be_visible()

    def check_submitted_from_is_visible(self) -> None:
        expect(self.submitted_form).to_be_visible()

    def check_submitted_from_is_not_visible(self) -> None:
        expect(self.submitted_form).not_to_be_visible()

    def check_submitted_text_is_(self, submitted_text: str) -> None:
        expect(self.submitted_form).to_have_text(submitted_text)

    @property
    def button_click(self) -> Locator:
        return self.page.get_by_role('button', name='Click')

    @property
    def submitted_form(self) -> Locator:
        return self.page.locator('#result')

    @property
    def tab_like_button(self) -> Locator:
        return self.page.get_by_role('link', name='Looks like a button')
