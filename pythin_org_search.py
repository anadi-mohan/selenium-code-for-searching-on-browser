from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
str=raw_input("Enter some question");
driver = webdriver.Chrome()
driver.get("https://www.google.com")
assert "Google" in driver.title
elem=driver.find_element_by_name("q")
elem.clear()
elem.send_keys(str+" quora")
elem.send_keys(Keys.RETURN)
element=driver.find_element(By.PARTIAL_LINK_TEXT,'quora');
element.click();