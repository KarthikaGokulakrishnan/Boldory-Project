from selenium.webdriver.common.by import By


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
