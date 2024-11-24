from fnmatch import translate
import os
from selenium import webdriver
from selenium.webdriver.common import service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait



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


driver.get("https://www.ign.es/WebServiceTransformCoordinates/")
wait = WebDriverWait(driver, 10)

# Changing the webpage to deal with UTM coordenates
type_of_coordenate_system = driver.find_element(By.ID, "sourceCRSCombo")
type_of_coordenate_system.send_keys("UTM")
type_of_coordenate_system.send_keys(Keys.RETURN)

# Putting X and Y coordenates into variables
x_coordenate = driver.find_element(By.ID, "inputX")
y_coordenate = driver.find_element(By.ID, "inputY")
# Putting the transform button into a variable
transform_button = driver.find_element(By.ID, "transformPoint")

# Result coordenates fields
longitudeDegree = driver.find_element(By.ID, "outputLongitudeDegree")
longitudeMinutes = driver.find_element(By.ID, "outputLongitudeMinutes")
longitudeSeconds = driver.find_element(By.ID, "outputLongitudeSeconds")

latitudeDegree = driver.find_element(By.ID, "outputLatitudeDegree")
latitudeMinutes = driver.find_element(By.ID, "outputLatitudeMinutes")
latitudeSeconds = driver.find_element(By.ID, "outputLatitudeSeconds")


# Type x and y coordenates
def type_new_coordenates(x: str, y: str):
    x_coordenate.clear()
    y_coordenate.clear()
    x_coordenate.send_keys(x)
    x_coordenate.send_keys(Keys.RETURN)
    y_coordenate.send_keys(y)
    y_coordenate.send_keys(Keys.RETURN)


## Wait function
def element_has_text(element):
    condition = element.get_attribute("value") != ""
    return condition
def retrieve_data():
    longitude = longitudeDegree.get_attribute("value") + " " + longitudeMinutes.get_attribute("value") + " " + longitudeSeconds.get_attribute("value")
    latitude = latitudeDegree.get_attribute("value") + " " + latitudeMinutes.get_attribute("value") + " " + latitudeSeconds.get_attribute("value")
    return (longitude, latitude)

def process_data(x: str, y: str):
    type_new_coordenates(x,y)
    transform_button.click()
    wait.until(lambda driver: element_has_text(longitudeDegree))
    
    return retrieve_data()


new_data = process_data("4321", "1234")
print("Longitud: " + new_data[0] + "\n" + "Latitud: " + new_data[1])
new_data = process_data("1000", "9999")
print("Longitud: " + new_data[0] + "\n" + "Latitud: " + new_data[1])

driver.close()
