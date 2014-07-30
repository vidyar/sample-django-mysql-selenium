from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

class FunctionalTest(LiveServerTestCase):
  @classmethod
  def setUpClass(cls):
    cls.selenium = WebDriver()
    super(FunctionalTest, cls).setUpClass()

  @classmethod
  def tearDownClass(cls):
    cls.selenium.quit()
    super(FunctionalTest, cls).tearDownClass()

  def test_index(self):
    self.selenium.get(self.live_server_url)
    header = self.selenium.find_element_by_tag_name('h1')
    self.assertRegexpMatches(header.text, r'Hello world, [0-9]+!')
