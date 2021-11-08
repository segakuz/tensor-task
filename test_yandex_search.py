from .pages.links import SearchPageLinks
from .pages.search_page import SearchPage
from .pages.search_result_page import SearchResultPage
import pytest


@pytest.mark.test_position
class TestYandexSearch():

    def test_yandex_search_result(self, browser):
        url = SearchPageLinks.SEARCH_PAGE_URL
        search_page = SearchPage(browser, url)

        search_page.open()
        search_page.should_be_search_field()
        search_page.fill_search_field()
        search_page.should_appear_suggestions_table()
        search_page.click_enter_key()

        result_page = SearchResultPage(browser, browser.current_url)
        result_page.should_appear_search_result()
        result_page.required_result_should_be_in_top_positions()
