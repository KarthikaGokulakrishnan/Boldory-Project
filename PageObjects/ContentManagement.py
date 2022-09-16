from selenium.webdriver.common.by import By
from PageObjects.Report import report_step

class ContentManagement:
    def __init__(self, driver):
        self.driver = driver

    contentmanagementmenu = (By.XPATH,"//button[2]/span/div[@class='contents-div']")
    scriptName = (By.CLASS_NAME,"script-name")
    approvedTab = (By.XPATH,"//div[@role='tab'][2]")
    searchBar = (By.XPATH, "//input[@placeholder='Search']")
    dotIcon = (By.XPATH,"//div/mat-icon")
    menuItem = (By.XPATH,"//button[@role='menuitem']")
    rejectionReason = (By.XPATH,"//textarea[@placeholder='Rejection Comment']")
    submitButton = (By.XPATH,"//button[@type='submit']")
    msg = (By.CLASS_NAME,"mat-simple-snack-bar-content")
    rejectedTab = (By.XPATH,"//div[@role='tab'][3]")
    categoryTab=(By.XPATH,"//div[@role='tab'][8]")
    addCategory=(By.XPATH,"//div/div/button[@type='button']")
    categoryName=(By.XPATH, "//input[@formcontrolname='categoryName']")
    imgupload=(By.XPATH,"//input[@class='file-input']")
    addButton=(By.XPATH,"//button[@type='submit']")
    deleteIcon=(By.XPATH,"//div[6]/div/mat-card/div/div/mat-icon[2]")
    suspendButton=(By.XPATH,"//span[text()=' SUSPEND ']")



    def getcontentmanagementmenu(self):
        return self.driver.find_element(*ContentManagement.contentmanagementmenu)

    def getscriptName(self):
        return self.driver.find_elements(*ContentManagement.scriptName)

    def getapprovedTab(self):
        return self.driver.find_element(*ContentManagement.approvedTab)


    def getsearchBar(self):
        return self.driver.find_element(*ContentManagement.searchBar)

    def getdotIcon(self):
        return self.driver.find_element(*ContentManagement.dotIcon)

    def getmenuItem(self):
        return self.driver.find_element(*ContentManagement.menuItem)

    def getsubmitButton(self):
        return self.driver.find_element(*ContentManagement.submitButton)

    def getrejectionReason(self):
        return self.driver.find_element(*ContentManagement.rejectionReason)

    def getmsg(self):
        return self.driver.find_element(*ContentManagement.msg)

    def getrejectedTab(self):
        return self.driver.find_element(*ContentManagement.rejectedTab)

    def getcategoryTab(self):
        return self.driver.find_element(*ContentManagement.categoryTab)

    def getaddCategory(self):
        return self.driver.find_element(*ContentManagement.addCategory)

    def getimgupload(self):
        return self.driver.find_element(*ContentManagement.imgupload)

    def getcategoryName(self):
        return self.driver.find_element(*ContentManagement.categoryName)

    def getaddButton(self):
        return self.driver.find_element(*ContentManagement.addButton)

    def getdeleteIcon(self):
        return self.driver.find_element(*ContentManagement.deleteIcon)

    def getsuspendButton(self):
        return self.driver.find_element(*ContentManagement.suspendButton)


# allure Steps Definition

    def ListOfScripts(self):
        report_step('Enter Script name in search bar')
        report_step('Get the list of searched Scripts')
        report_step('Assert with one script name which is present in List')

    def RejectScript(self):
        report_step('Go to Approved Tab')
        report_step('Enter Script name in search bar')
        report_step('Click on the 3 dot icon')
        report_step('Click on Reject')
        report_step('Verify that script is rejected')

    def ApproveScript(self):
        report_step('Go to Rejected Tab')
        report_step('Enter Script name in search bar')
        report_step('Click on the 3 dot icon')
        report_step('Click on Approve')
        report_step('Verify that script is Approved and removed from the list')

    def Addcategory(self):
        report_step('Go to category Tab')
        report_step('Click on add category option')
        report_step('Upload img')
        report_step('Enter category name')
        report_step('Click on add Button')
        report_step('Verify that category is created')
        report_step('Click on the delete icon')
        report_step('Click on suspend Button')
        report_step('Verify that category is suspended')












    def ListOfScripts(self):
        report_step('Enter User name in search bar')
        report_step('Get the list of searched User')
        report_step('Assert with one user name which is present in another user')