from pages.main_page import MainPage


def test_simple_button_is_visible(f_main_page: MainPage) -> None:
    main_page = f_main_page
    buttons_page = main_page.click_link_simple_button()
    buttons_page.check_button_click_is_visible()


def test_simple_button_is_not_submitted(f_main_page: MainPage) -> None:
    main_page = f_main_page
    buttons_page = main_page.click_link_simple_button()
    buttons_page.check_submitted_from_is_not_visible()


def test_click_simple_button(f_main_page: MainPage) -> None:
    main_page = f_main_page
    buttons_page = main_page.click_link_simple_button()
    buttons_page.click_button_click()
    buttons_page.check_submitted_from_is_visible()
    buttons_page.check_submitted_text_is_('Submitted')


def test_like_button_is_visible(f_main_page: MainPage) -> None:
    main_page = f_main_page
    simple_button_page = main_page.click_link_simple_button()
    like_button_page = simple_button_page.click_tab_like_button()
    like_button_page.check_like_button_is_visible()


def test_like_button_is_not_submitted(f_main_page: MainPage) -> None:
    main_page = f_main_page
    simple_button_page = main_page.click_link_simple_button()
    like_button_page = simple_button_page.click_tab_like_button()
    like_button_page.check_submitted_from_is_not_visible()


def test_click_like_button(f_main_page: MainPage) -> None:
    main_page = f_main_page
    simple_button_page = main_page.click_link_simple_button()
    like_button_page = simple_button_page.click_tab_like_button()
    like_button_page.click_like_button()
    like_button_page.check_submitted_form_is_visible()
    like_button_page.check_submitted_text_is_('Submitted')
