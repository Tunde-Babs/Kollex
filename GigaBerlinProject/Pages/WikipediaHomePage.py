class WikepediaHome():

    def __init__(self, driver):
        self.driver = driver

        self.search_textbox_id = "searchInput"
        self.search_button_xpath = "//*[@id='search-form']/fieldset/button"

    def search_giga_berlin(self):
        assert "Wikipedia" in self.driver.title
        self.driver.find_element_by_id(self.search_textbox_id).send_keys("Giga Berlin")
        self.driver.find_element_by_xpath(self.search_button_xpath).click()