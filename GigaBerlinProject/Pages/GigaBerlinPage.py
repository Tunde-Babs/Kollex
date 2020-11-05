class GigaBerlin():

    def __init__(self, driver):
        self.driver = driver

        self.location_on_map_link_xpath = "//*[@id='mw-content-text']/div[1]/table[1]/tbody/tr[2]/td/a/img"

    def page_content_search(self):
        coordinates = self.driver.page_source
        assert "52.4°N 13.8°E" in coordinates

        logistics = self.driver.find_element_by_tag_name('body').text
        assert "Logistics" in logistics

        site_concerns = self.driver.find_element_by_tag_name('body').text
        assert "Site concerns" in site_concerns
