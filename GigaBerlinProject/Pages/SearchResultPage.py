class SearchResultPage():

    def __init__(self, driver):
        self.driver = driver

        self.google_search_result_xpath = "//*[@id='rso']/div[1]/div/div[1]/a/div/cite"

    def click_wikipedia(self):
        page_content = self.driver.page_source
        assert "www.wikipedia.org" in page_content
        self.driver.find_element_by_xpath(self.google_search_result_xpath).click()



