from typing import List

from selenium.webdriver.remote.webelement import WebElement


class Utils:

    @staticmethod
    def join_string(elements: List[WebElement]):
        return ', '.join(elements)
