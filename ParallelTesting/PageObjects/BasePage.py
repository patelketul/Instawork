from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import time


class BasePage():

    #Wait for element to be visible
    def waitForElement(self, driver,locator,wait=30):
        return WebDriverWait(driver, wait).until(EC.visibility_of_element_located(locator))

    # Get element
    def getElement(self, driver, locator, wait=30):
        # typeOfLocator = locator[0] #Get type of locator i.e. ID, XPATH, CLASS_NAME etc
        # elementPath = locator[1] #Get locator of element
        WebDriverWait(driver, wait).until(EC.visibility_of_element_located(locator))

        time.sleep(1)

        if (locator[0] == "id"):
            element = driver.find_element_by_id(locator[1])
            return element

        elif (locator[0] == "xpath"):
            element = driver.find_element_by_xpath(locator[1])
            return element

        elif (locator[0] == "link_text"):
            element = driver.find_element_by_link_text(locator[1])
            return element

        elif (locator[0] == "partial link text"):
            element = driver.find_element_by_partial_link_text(locator[1])
            return element

        elif (locator[0] == "name"):
            element = driver.find_element_by_name(locator[1])
            return element

        elif (locator[0] == "tag name"):
            element = driver.find_element_by_tag_name(locator[1])
            return element

        elif (locator[0] == "class name"):
            element = driver.find_element_by_class_name(locator[1])
            return element

        elif (locator[0] == "css selector"):
            element = driver.find_element_by_css_selector(locator[1])
            return element

    #Wait for element and click
    def waitAndClick(self, driver, locator):
        self.waitForElement(driver, locator)
        self.getElement(driver, locator).click()

    # Wait for element to render and type text
    def waitAndType(self, driver, text, locator):
        self.waitForElement(driver, locator)
        self.getElement(driver, locator).send_keys(text)

    # Check of element is present or not
    def isElementPresent(self, driver, locator, wait=30):
        try:
            self.waitForElement(driver, locator, wait)
            self.getElement(driver, locator).is_displayed()
            return True
        except:
            return False

    #Get all elements matching locator
    def getAllElements(self,driver,locator):
        return driver.find_elements_by_xpath(locator[1])

    # CLick on the element
    def clickElement(self, element):
        time.sleep(3)
        element.click()

    #Check if child is present inside parent or not
    def isChildPresentInParent(self,driver,parent,child):
        try:
            parent.find_element_by_xpath(child[1])
            return True
        except:
            return False