from .base_page import BasePage
from .locators import ImagesPageLocators
from .locators import ImagesSearchPageLocators
from urllib.parse import urlparse
from urllib.parse import parse_qs


class ImagesSearchPage(BasePage):

    def __init__(self, browser, url, category_name, timeout=5):
        super().__init__(browser, url, timeout)
        self.category_name = category_name

    def category_page_should_be_opened_successfully(self):
        self.should_be_category_name_in_search_field()
        self.should_be_images_grid()

    def should_be_category_name_in_search_field(self):
        print(f'Проверяем, что в поиске введён текст открытой категории "{self.category_name}"')

        search_field = self.browser.find_element(*ImagesPageLocators.SEARCH_FIELD)
        text_in_search_field = search_field.get_attribute('value')

        assert self.category_name in text_in_search_field, 'Search field does not contain category_name'

    def should_be_images_grid(self):
        print('Проверяем, что присутствует таблица с результатами (картинками)')

        assert self.is_element_present(*ImagesSearchPageLocators.IMAGES_GRID), "Images grid is not presented"

    def open_first_image(self):
        print('Открываем первую картинку')

        first_image = self.browser.find_element(*ImagesSearchPageLocators.FIRST_IMAGE)
        self.first_image_url = first_image.get_attribute('href')
        first_image.click()


    def first_image_should_be_opened_successfully(self):
        self.should_be_image_view()
        self.should_be_image_url_in_opened_url()


    def should_be_image_url_in_opened_url(self):
        print('Проверяем, что адрес картинки присутствует в параметрах запроса в текущем url')

        img_url_qs = parse_qs(urlparse(self.first_image_url).query)
        opened_url_qs = parse_qs(urlparse(self.browser.current_url).query)

        if 'img_url' in img_url_qs and 'img_url' in opened_url_qs:
            assert img_url_qs['img_url'][0] == opened_url_qs['img_url'][0], 'Current url contains incorrect image url'
        else:
            assert False, 'Current url does not contain image url'

    def should_be_image_view(self):
        print('Проверяем, что на странице открыта картинка')

        assert self.is_element_present(*ImagesSearchPageLocators.IMAGE_VIEW), 'Image view is not presented'


    def should_be_different_image_if_click_next_button(self):
        print('Проверяем, что при нажатии кнопки вперёд картинка меняется')

        self.first_image_src = self.browser.find_element(*ImagesSearchPageLocators.IMAGE_VIEW).get_attribute('src')
        self.click_next_button()

        second_image_src = self.browser.find_element(*ImagesSearchPageLocators.IMAGE_VIEW).get_attribute('src')

        assert self.first_image_src != second_image_src, 'Images are the same, but should not be'

    def should_be_first_image_if_click_prev_button(self):
        print('Проверяем, что при нажатии кнопки назад картинка меняется на первоначальную')

        self.click_prev_button()
        current_image_src = self.browser.find_element(*ImagesSearchPageLocators.IMAGE_VIEW).get_attribute('src')

        assert self.first_image_src == current_image_src, 'Should be the first image, but it is not'


    def click_next_button(self):
        next_button = self.browser.find_element(*ImagesSearchPageLocators.NEXT_BUTTON)
        next_button.click()

    def click_prev_button(self):
        prev_button = self.browser.find_element(*ImagesSearchPageLocators.PREV_BUTTON)
        prev_button.click()
