from selenium.webdriver.common.keys import Keys
from .locators import SearchPageLocators
from .base_page import BasePage


class SearchPage(BasePage):

    def should_be_search_field(self):
        print('Проверяем наличие поля для поиска')

        assert self.is_element_present(*SearchPageLocators.SEARCH_FIELD), \
            'Input field for searching is not presented'

    def fill_search_field(self, text = 'Тензор'):
        print(f'Вводим в поиск {text}')

        input = self.browser.find_element(*SearchPageLocators.SEARCH_FIELD)
        input.send_keys(text)

    def should_appear_suggestions_table(self):
        print('Проверяем, что появилась таблица с подсказками')

        assert self.is_element_appeared(*SearchPageLocators.SUGGESTIONS_TABLE), \
            'Table of suggestions did not appear'

    def click_enter_key(self):
        print('Нажимаем клавишу Enter')

        input = self.browser.find_element(*SearchPageLocators.SEARCH_FIELD)
        input.send_keys(Keys.ENTER)

    def should_be_images_link(self):
        print('Проверяем, что ссылка "{}" присутствует на странице'.format(SearchPageLocators.IMAGES_LINK[1]))

        assert self.is_element_present(*SearchPageLocators.IMAGES_LINK), \
            'Link to images page is not presented'

    def go_to_images_page(self):
        print('Кликаем на ссылку')

        images_link = self.browser.find_element(*SearchPageLocators.IMAGES_LINK)
        images_link.click()

        new_tab = self.browser.window_handles[1]
        self.browser.switch_to.window(new_tab)
