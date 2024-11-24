import os
from selenium import webdriver
from selenium.webdriver.common import service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService

#Provide the path to the firefox webdriver
geckodriver_path = os.path.join(os.path.dirname(__file__), "../../../geckodriver")

install_dir = "/usr/bin"
binary_loc = os.path.join(install_dir, "firefox")

#Instantiate a service with the driver
service = FirefoxService(geckodriver_path)
opts = webdriver.FirefoxOptions()
opts.binary_location = binary_loc
opts.add_argument("-profile")
opts.add_argument("/home/ayuda106/snap/firefox/common/.mozilla/firefox/1hjffc8i.selenium-profile")
#Assign the service to the driver and the options
driver = webdriver.Firefox(service=service, options=opts)


driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
