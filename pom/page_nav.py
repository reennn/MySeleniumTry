from base.selenium_base import SeleniumBase
from base.utils import Utils
from selenium.webdriver.support import expected_conditions as ec


class PageNav(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav_link = '#searchInput'
        self.nav_link_name = 'SearchBar'
        self.expected_nav_h1 = 'Python'

    def __get_nav_links(self):
        return self.is_visible('css', self.nav_link, self.nav_link_name)

    def get_nav_link_text(self):
        nav_links = self.__get_nav_links()
        nav_links_text = self.get_text_from_webelements(nav_links)
        return Utils.join_string(nav_links_text)

    def send_keys(self, search_info: str):
        nav_link = self.__get_nav_links()
        nav_link.send_keys(search_info)

    def submit_button(self):
        button = self.__get_nav_links()
        button.submit()

