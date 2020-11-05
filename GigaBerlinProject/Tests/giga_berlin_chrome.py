import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class SearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        Path = "C:/Program Files/Drivers/chromedriver.exe"
        cls.driver = webdriver.Chrome(Path)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_google_page_title(self):
        driver = self.driver

        accept_cookies_css = "#introAgreeButton .RveJvd"
        driver.get("https://www.google.com/")
        driver.switch_to.frame(0)
        driver.find_element_by_css_selector(accept_cookies_css).click()
        google_page_title = driver.title
        assert "Google" in google_page_title
        driver.save_screenshot("GigaBerlinProject/Screenshots/google_homepage.png")

    #Using the google search box to query "Wikipedia.org"

    #def search_wikipedia(wiki):

        #driver = wiki.driver

        search_textbox_name = "q"
        driver.find_element_by_name(search_textbox_name).send_keys("www.wikipedia.org")
        driver.save_screenshot("GigaBerlinProject/Screenshots/wikipedia_search.png")
        driver.find_element_by_name(search_textbox_name).send_keys(Keys.ENTER)

   # def google_search_result(result):
     #   driver = result.driver

        google_search_result_xpath = "//*[@id='rso']/div[1]/div/div[1]/a/div/cite"
        page_content = driver.page_source
        assert "www.wikipedia.org" in page_content
        driver.find_element_by_xpath(google_search_result_xpath).click()

   # def wikipedia_home_page(home):
    #    driver = home.driver

        # Testing to validate wikipedia website was correctly navigated by the page title
        assert "Wikipedia" in driver.title
        driver.save_screenshot("GigaBerlinProject/Screenshots/wikipedia_homepage.png")

  #  def search_giga_berlin(giga):
    #    driver = giga.driver

        search_textbox_id = "searchInput"
        search_button_xpath = "//*[@id='search-form']/fieldset/button"

        assert "Wikipedia" in driver.title
        driver.find_element_by_id(search_textbox_id).send_keys("Giga Berlin")

        driver.save_screenshot("GigaBerlinProject/Screenshots/giga_berlin_search.png")

        driver.find_element_by_xpath(search_button_xpath).click()

   # def giga_berlin_page(content):
   #     driver = content.driver

        # Testing that expected redirection was made to the Giga_Berlin article-page
        current_url = driver.current_url
        assert "https://en.wikipedia.org/wiki/Giga_Berlin" in current_url

        # Testing for the coordinate on the web page
        coordinates = driver.page_source
        assert "52.4°N 13.8°E" in coordinates

        # Testing that the word 'Logistics' (especially with a uppercase 'L') is contained in the body of the article
        logistics = driver.find_element_by_tag_name('body').text
        assert "Logistics" in logistics

        # Testing that 'Site concerns' was equally contained in the body of the web page
        site_concerns = driver.find_element_by_tag_name('body').text
        assert "Site concerns" in site_concerns

        driver.save_screenshot("GigaBerlinProject/Screenshots/giga_berlin_article.png")

  #  def map_location_in_new_tab(map):
   #     driver = map.driver

        location_on_map_link_xpath = "//*[@id='mw-content-text']/div[1]/table[1]/tbody/tr[2]/td/a/img"

        # Opens a new tab then redirects to the Giga Berlin location on the Map

        map_location_link = driver.find_element_by_xpath(location_on_map_link_xpath)
        site_view = map_location_link.click()

        # This launches a new tab and then queries the site location there
        driver.execute_script("window.open('%s', '_blank')" % site_view)

        # Testing that correct url is being navigated, to capture the site location on the map
        map_url = driver.current_url
        assert "https://en.wikipedia.org/wiki/Giga_Berlin#/map/0" in map_url

        driver.save_screenshot("GigaBerlinProject/Screenshots/map_location.png")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main()
