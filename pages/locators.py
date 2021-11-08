from selenium.webdriver.common.by import By


class SearchPageLocators():
    SEARCH_FIELD = (By.CSS_SELECTOR, 'input#text')
    SUGGESTIONS_TABLE = (By.CSS_SELECTOR, '.mini-suggest__popup_visible > ul.mini-suggest__popup-content')
    IMAGES_LINK = (By.LINK_TEXT, 'Картинки')
    IMAGES_BUTTON = (By.CSS_SELECTOR, 'a[data-id="images"]')

class SearchResultPageLocators():
    SEARCH_RESULT_LIST = (By.CSS_SELECTOR, 'ul#search-result')
    SEARCH_RESULT_ITEMS = (By.XPATH, "//ul[@id='search-result']/li[contains(@class, 'serp-item') and not(contains(@data-fast-name, 'suggest_fact'))][position() <= 5]")
    TENSOR_LINK = (By.LINK_TEXT, 'tensor.ru')

class ImagesPageLocators():
    FIRST_CATEGORY = (By.CSS_SELECTOR, '.PopularRequestList-Item:first-child a')
    SEARCH_FIELD = (By.CSS_SELECTOR, '.search2__input input')

class ImagesSearchPageLocators():
    IMAGES_GRID = (By.CSS_SELECTOR, 'div.serp-list[role="list"]')
    FIRST_IMAGE = (By.CSS_SELECTOR, 'div.serp-item[role="listitem"]:first-child a')
    IMAGE_VIEW = (By.CSS_SELECTOR, '.MediaViewer-View .MMImage-Preview')
    NEXT_BUTTON = (By.CSS_SELECTOR, '.MediaViewer-ButtonNext')
    PREV_BUTTON = (By.CSS_SELECTOR, '.MediaViewer-ButtonPrev')
