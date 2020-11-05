from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


#Path = "C:\Program Files\Drivers\chromedriver.exe" # path to the browser instance
#driver = webdriver.Chrome(Path)# webdriver directed to my browser instance path

#Path = "C:\Program Files\Drivers\msedgedriver.exe"
#driver = webdriver.Edge(Path)

Path = "C:\Program Files\Drivers\chromedriver.exe"
driver = webdriver.Chrome(Path)

driver.implicitly_wait(10)
driver.maximize_window()

# Accepting cookies pop up
driver.get("https://www.google.com/")
driver.switch_to.frame(0)
driver.find_element_by_css_selector("#introAgreeButton .RveJvd").click()

# Testing the web page title as "Google"
assert "Google" in driver.title

driver.save_screenshot("GigaBerlinProject/Screenshots/google_homepage.png")

#search for the wikipedia.org
driver.find_element_by_name("q").send_keys("www.wikipedia.org")

driver.save_screenshot("GigaBerlinProject/Screenshots/wikipedia_search.png")

driver.find_element_by_name("q").send_keys(Keys.ENTER)

# search result page
page_content = driver.page_source
assert "www.wikipedia.org" in page_content
driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div[1]/a/div/cite").click()


# Testing to validate wikipedia website was correctly navigated by the page title
assert "Wikipedia" in driver.title
driver.save_screenshot("GigaBerlinProject/Screenshots/wikipedia_homepage.png")

driver.find_element_by_id("searchInput").send_keys("Giga Berlin")

driver.save_screenshot("GigaBerlinProject/Screenshots/giga_berlin_search.png")

driver.find_element_by_xpath("//*[@id='search-form']/fieldset/button").click()

# Testing for the coordinate on the web page
coordinates = driver.page_source
assert "52.4°N 13.8°E" in coordinates

# Testing that the word 'Logistics' (especially with a uppercase 'L') is contained in the body of the article
logistics = driver.find_element_by_tag_name('body').text
assert "Logistics" in logistics

# Testing that 'Site concerns' was equally contained in the body of the web page
site_concerns = driver.find_element_by_tag_name('body').text
assert "Site concerns" in site_concerns

# Testing that expected redirection was made to the Giga_Berlin article-page
current_url = driver.current_url
assert "https://en.wikipedia.org/wiki/Giga_Berlin" in current_url

driver.save_screenshot("GigaBerlinProject/Screenshots/giga_berlin_article.png")


# Opens a new tab then redirects to the Giga Berlin location on the Map

map_location_link = driver.find_element_by_xpath("//*[@id='mw-content-text']/div[1]/table[1]/tbody/tr[2]/td/a/img")
site_view = map_location_link.click()

driver.execute_script("window.open('%s', '_blank')" % site_view)

# Testing that correct url is being navigated, to capture the site location on the map
map_url = driver.current_url
assert "https://en.wikipedia.org/wiki/Giga_Berlin#/map/0" in map_url
time.sleep(2)
driver.save_screenshot("GigaBerlinProject/Screenshots/map_location.png")

time.sleep(2)
driver.quit()
print("A total of 7 tests were Completed and Passed")