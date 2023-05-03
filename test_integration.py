from selenium.webdriver.chrome.webdriver import WebDriver

from django.test import LiveServerTestCase

class Hosttest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = WebDriver("./other_files/cdriver/chromedriver/chromedriver")
        cls.driver.implicitly_wait(1000)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_home_page(self):
        self.driver.get(f"{self.live_server_url}/blog/")
        assert "My Blog" in self.driver.title