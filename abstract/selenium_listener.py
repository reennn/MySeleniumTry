from selenium.webdriver.support.events import AbstractEventListener

from base.selenium_base import SeleniumBase


class MyListener(AbstractEventListener):

    def after_click(self, element, driver) -> None:
        pass
