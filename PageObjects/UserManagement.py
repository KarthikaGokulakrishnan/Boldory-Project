from selenium.webdriver.common.by import By

from PageObjects.Report import report_step


class UserManagement:
    def __init__(self,driver):
        self.driver = driver

    SearchID=(By.XPATH,"//input[@placeholder='Search']")
    username=(By.XPATH,"//tr/td[1]")
    dotIcon=(By.XPATH, "//tr[1]/td[4]/div/mat-icon")
    menuItem2=(By.XPATH, "//button[@role='menuitem'][2]")
    textarea=(By.XPATH, "//div/textarea[@data-placeholder='Type your message...']")
    sendButton=(By.XPATH, "//button[@type='submit']")
    snackmsg=(By.XPATH, "//span[@class='mat-simple-snack-bar-content']")
    menuItem1=(By.XPATH, "//button[@role='menuitem'][1]")
    status=(By.XPATH,"//tr[1]/td[3]/div[@class='ng-star-inserted']")
    tab=(By.XPATH,"//div[@role='tab'][2]")
    AddButton=(By.XPATH,"//button[@class='mat-focus-indicator button mat-raised-button mat-button-base ng-star-inserted']")
    Firstname=(By.XPATH,"//input[@placeholder='First Name']")
    LastName=(By.XPATH,"//input[@placeholder='Last Name']")
    EmailID=(By.XPATH, "//input[@placeholder='Email']")
    Password=(By.XPATH, "//input[@placeholder='Password']")
    createButton=(By.XPATH, "//button[@type='submit']")
    adminMenuItem=(By.XPATH,"//button[@role='menuitem']")
    adminStatus=(By.XPATH,"//tr[2]/td[3]/div[@class='ng-star-inserted']")
    AdminDotIcon=(By.XPATH,"//tr[2]/td[4]/div/mat-icon[1]")

    def getSearchText(self):
        return self.driver.find_element(*UserManagement.SearchID)

    def getSearchList(self):
        return self.driver.find_elements(*UserManagement.username)

    def getdotIcon(self):
        return self.driver.find_element(*UserManagement.dotIcon)

    def getmenuItem2(self):
        return self.driver.find_element(*UserManagement.menuItem2)

    def getTextarea(self):
        return self.driver.find_element(*UserManagement.textarea)

    def getsendButton(self):
        return self.driver.find_element(*UserManagement.sendButton)

    def getSnackMsg(self):
        return self.driver.find_element(*UserManagement.snackmsg)

    def getmenuItem1(self):
        return self.driver.find_element(*UserManagement.menuItem1)

    def getStatus(self):
        return self.driver.find_element(*UserManagement.status)
    def getTab(self):
        return self.driver.find_element(*UserManagement.tab)
    def getAddButton(self):
        return self.driver.find_element(*UserManagement.AddButton)

    def getFirstName(self):
        return self.driver.find_element(*UserManagement.Firstname)

    def getLastName(self):
        return self.driver.find_element(*UserManagement.LastName)

    def getEmail(self):
        return self.driver.find_element(*UserManagement.EmailID)

    def getPassword(self):
        return self.driver.find_element(*UserManagement.Password)

    def getCreateButton(self):
        return self.driver.find_element(*UserManagement.createButton)

    def getAddadminMenuItem(self):
        return self.driver.find_element(*UserManagement.adminMenuItem)

    def getAdminStatus(self):
        return self.driver.find_element(*UserManagement.adminStatus)

    def getAdmindotIcon(self):
        return self.driver.find_element(*UserManagement.AdminDotIcon)
   #Allure step function


    def SearchUser(self):
        report_step('Enter User name in search bar')
        report_step('Get the list of searched User')
        report_step('Assert with one user name which is present in another user')
    def SendNotification(self):
        report_step('Select the User')
        report_step('Click on the send Notification option')
        report_step('Enter Text message')
        report_step('Click on Send Button')
    def SuspendUser(self):
        report_step('Select the User')
        report_step('Click on the suspend option')
        report_step('Verify User suspended')
        report_step('Select the suspended User')
        report_step('Click on the active option')
        report_step('Verify User Activated')
    def AddAdmin(self):
        report_step('Go To Admin Tab')
        report_step('Click on the add admin option')
        report_step('Enter First Name')
        report_step('Enter Last name')
        report_step('Enter Email ID')
        report_step('Enter Password')
        report_step('Click on Create Button')
    def SuspendAdmin(self):
        report_step('Select the Admin')
        report_step('Click on the suspend option')
        report_step('Verify Admin suspended')
        report_step('Select the suspended Admin')
        report_step('Click on the active option')
        report_step('Verify Admin Activated')