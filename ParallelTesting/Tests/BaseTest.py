from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BaseTest():

    def startDriver(self,browser):
        # Change platform if tests are required to run on platform other then MAC
        return webdriver.Remote(desired_capabilities={"browserName": browser, "platform":"MAC", "node":"5556"})


