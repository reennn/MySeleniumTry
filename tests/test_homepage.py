import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pom.page_nav import PageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_nav_links(self):
        page_nav = PageNav(self.driver)

        page_nav.send_keys('Python')
        page_nav.submit_button()

        time.sleep(5)

