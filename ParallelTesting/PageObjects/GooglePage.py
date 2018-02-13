import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from PageObjects.BasePage import BasePage


class GooglePage():

    basePage = BasePage()
    searchText = (By.ID,"lst-ib")
    searchResultList = (By.ID, "rso")
    searchResultLink = (By.XPATH, "//cite[@class='_Rm' and contains(.,'https://www.instawork.com/')]")
    searchResultBlock = (By.XPATH, "//div[@class='g']")
    searchResultLinkchild = (By.XPATH, ".//cite[@class='_Rm' and contains(.,'https://www.instawork.com/')]")

    footerPageLinks = (By.XPATH,"//div[@id='foot']//a")

    #Enter search term in search textbox
    def enterSearchTerm(self,driver,searchTerm):
        self.basePage.waitAndType(driver, searchTerm, self.searchText)

    #Press "Enter" key on search textbox
    def pressEnterKeySearchBox(self,driver):
        self.basePage.getElement(driver,self.searchText).send_keys(Keys.RETURN)
        self.basePage.waitForElement(driver,self.searchResultList)

    #Verify if search result is present in the result page
    def isSearchResultPresentInFirst(self,driver):
        return self.basePage.isElementPresent(driver,self.searchResultLink)

    # get the order(position) of search term in search result page
    def getOrderOfSearchResult(self,driver):

        self.basePage.waitForElement(driver,self.searchResultList)
        searchBlocks = self.basePage.getAllElements(driver,self.searchResultBlock)

        for i in xrange(len(searchBlocks)):
            if self.basePage.isChildPresentInParent(driver,searchBlocks[i],self.searchResultLinkchild) is True:
                return i+1
            else:
                continue

    #Get total number of search result pages
    def getNumberOfSearchPages(self,driver):
        return len(self.basePage.getAllElements(driver,self.footerPageLinks))

    def getAllPagelinks(self,driver):
        return self.basePage.getAllElements(driver,self.footerPageLinks)

    def clickOnPageLink(self,driver,pageLink):
        self.basePage.clickElement(pageLink)






