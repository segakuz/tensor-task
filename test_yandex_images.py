
from .pages.images_page import ImagesPage
from .pages.images_search_page import ImagesSearchPage
from .pages.links import SearchPageLinks
from .pages.search_page import SearchPage
import pytest

@pytest.mark.test_images
class TestYandexImages():

    def test_yandex_images_tab(self, browser):
        url = SearchPageLinks.SEARCH_PAGE_URL
        search_page = SearchPage(browser, url)

        search_page.open()
        search_page.should_be_images_link()
        search_page.go_to_images_page()

        images_page = ImagesPage(browser, browser.current_url)
        images_page.should_be_images_url()
        category_name = images_page.open_first_category()

        images_search_page = ImagesSearchPage(browser, browser.current_url, category_name)
        images_search_page.category_page_should_be_opened_successfully()
        images_search_page.open_first_image()
        images_search_page.first_image_should_be_opened_successfully()
        images_search_page.should_be_different_image_if_click_next_button()
        images_search_page.should_be_first_image_if_click_prev_button()
