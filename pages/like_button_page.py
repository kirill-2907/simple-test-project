from playwright.sync_api import Locator, expect

from pages.base_page import BasePage


class LikeButtonPage(BasePage):

    def check_like_button_is_visible(self) -> None:
        expect(self.like_button).to_be_visible()

    def check_submitted_from_is_not_visible(self) -> None:
        expect(self.submitted_form).not_to_be_visible()

    def click_like_button(self) -> None:
        self.like_button.click()

    def check_submitted_form_is_visible(self) -> None:
        expect(self.submitted_form).to_be_visible()

    def check_submitted_text_is_(self, text: str) -> None:
        expect(self.submitted_form).to_have_text(text)

    @property
    def like_button(self) -> Locator:
        return self.page.get_by_role('link', name='Click')

    @property
    def submitted_form(self) -> Locator:
        return self.page.locator('#result')
