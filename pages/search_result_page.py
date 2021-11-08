from .locators import SearchResultPageLocators
from .base_page import BasePage


class SearchResultPage(BasePage):

    def should_appear_search_result(self):
        print('Проверяем, что появилась таблица с результатами поиска')

        assert self.is_element_appeared(*SearchResultPageLocators.SEARCH_RESULT_LIST), \
            'Search result did not appear'

    def required_result_should_be_in_top_positions(self):
        print('Проверяем, что в первых 5 результатах есть ссылка на {}'.format(SearchResultPageLocators.TENSOR_LINK[1]))

        results = self.browser.find_elements(*SearchResultPageLocators.SEARCH_RESULT_ITEMS)

        in_top_positions = False

        for result in results:
            if self.is_element_present_in_element(result, *SearchResultPageLocators.TENSOR_LINK):
                in_top_positions = True
                break

        assert in_top_positions, 'Tensor is not appeared in top positions of search result'
