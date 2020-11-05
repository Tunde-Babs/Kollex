class GooglePage():

    def __init__(self, driver):
        self.driver = driver

        self.accept_cookies_css = "#introAgreeButton .RveJvd"
        self.search_textbox_name = "q"

    def accept_cookies(self):
        self.driver.get("https://www.google.com/")
        self.driver.switch_to.frame(0)
        self.driver.find_element_by_css_selector("self.accept_cookies_css").click()
        assert "Google" in self.driver.title

    def search_wikipedia(self):
        self.driver.find_element_by_name(self.search_textbox_name).send_keys("www.wikipedia.org")
        self.driver.find_element_by_name(self.search_textbox_name).send_keys(Keys.ENTER)
