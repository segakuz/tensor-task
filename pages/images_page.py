from .base_page import BasePage
from .locators import ImagesPageLocators
from .links import ImagesPageLinks


class ImagesPage(BasePage):

    def should_be_images_url(self):
        print('Проверяем, что перешли на url {}'.format(ImagesPageLinks.IMAGES_PAGE_URL))

        current_url = self.browser.current_url

        assert current_url.startswith(ImagesPageLinks.IMAGES_PAGE_URL), 'There is an incorrect images page url.'

    def open_first_category(self):
        first_category_element = self.browser.find_element(*ImagesPageLocators.FIRST_CATEGORY)
        category_name = first_category_element.text
        print(f'Открываем первую категорию "{category_name}"')

        first_category_element.click()
        return category_name
