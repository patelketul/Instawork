import subprocess, unittest, sys, time, os
sys.path.append(str((os.path.abspath(__file__))).split("ParallelTesting")[0] + "ParallelTesting")
from Tests.BaseTest import BaseTest
from PageObjects.GooglePage import GooglePage


# Enable "Allow Remote Automation" for safari

class FirstTest(unittest.TestCase):
    baseTest = BaseTest()
    googlePage = GooglePage()

    # Setup method to initiate webdriver
    def setUp(self):
        # self.start_hub_server = subprocess.Popen(['java -jar ../Selenium/selenium-server-standalone-3.6.0.jar -host http://localhost -port 4444 -role hub'],shell=True,stdout=None,stderr=None)
        # self.start_node_server = subprocess.Popen(['java -Dwebdriver.gecko.driver="../Selenium/geckodriver" -Dwebdriver.chrome.driver="../Selenium/chromedriver" -jar ../Selenium/selenium-server-standalone-3.6.0.jar -role webdriver -hub http://localhost:4444/grid/register -debug -port 5556 -browser browserName=firefox,maxInstances=5,platform=MAC -browser browserName=chrome,maxInstances=5,platform=MAC -browser browserName=safari,maxInstances=5,platform=MAC'],shell=True,stdout=None,stderr=None)

        # This code is by default set to run on MAC. If in case platform is different change MAC to WINDOWS/LINUX/UNIX
        # self.driver = webdriver.Remote(desired_capabilities={"browserName": browser, "platform":"MAC", "node":"5556"})
        self.driver = self.baseTest.startDriver(browser)

    # Test to verify search result comes first in the list. If result is not at first position give position
    def test_VerifyPositionInSearchResult(self):
        self.driver.get("http://www.google.com") #Open google page
        self.googlePage.enterSearchTerm(self.driver, searchTerm) #Enter search term
        self.googlePage.pressEnterKeySearchBox(self.driver) #Hit Enter
        order = self.googlePage.getOrderOfSearchResult(self.driver) #Find position of record. If record is not present function will return None
        if order != None: #if result is not present on the first page skip
            self.assertTrue(order == 1, "Result was found at " + str(order) + " location")
        else: #this portion of code will look result in remaining search pages (it will search in first 10 pages only)
            pagelinks = self.googlePage.getAllPagelinks(self.driver) #Get all search result page link
            for j in xrange(self.googlePage.getNumberOfSearchPages(self.driver)): # Loop through all links
                self.googlePage.clickOnPageLink(self.driver,pagelinks[j]) # Click on link to open
                if self.googlePage.isSearchResultPresentInFirst(self.driver) is True: #Search for Instaworks.com link in search
                    print "Search result was found in page "+str(j+2) # If link is present print on screen and exit
                    return
                else:
                    continue #If result is not present continue loop[
            print "Result was not found in first 10 pages"

    # Once test is completed close driver instance
    def tearDown(self):
        # self.start_hub_server.terminate()
        # self.start_node_server.terminate()
        self.driver.quit()


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 2:  # this is the case when search term is not passed while running tests
        browser = args[1]
        searchTerm = "Instawork"  # Take Instawork as default search term
    if len(args) == 3:  # this is the case when search term is passed while running tests
        browser = args[1]
        searchTerm = args[2]

    finder = unittest.TestLoader().loadTestsFromTestCase(FirstTest) #Create testsute
    unittest.TextTestRunner(verbosity=2).run(finder) #Run test
