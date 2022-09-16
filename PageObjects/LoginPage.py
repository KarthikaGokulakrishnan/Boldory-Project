from selenium.webdriver.common.by import By

from PageObjects.Report import report_step


class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    Email = (By.XPATH,"//input[@formcontrolname='emailSignin']")
    Password = (By.XPATH,"//input[@formcontrolname='passwordSignin']")
    SignIn =(By.XPATH,"//span[text()=' SIGN IN ']")
    BSText=(By.XPATH,"//div[text()='BOLDORY USERS']")
    Textarea=(By.XPATH, "//div/textarea[@data-placeholder='Type your message...']")


    def getEmail(self):
        return self.driver.find_element(*LoginPage.Email)
    def getPassword(self):
        return self.driver.find_element(*LoginPage.Password)
    def getSignInButton(self):
        return self.driver.find_element(*LoginPage.SignIn)
    def getBSText(self):
        return self.driver.find_element(*LoginPage.BSText)

    def go_to_login_page(self):
        report_step('Go to login page')

    def insert_user_name(self):
        report_step('Insert Username')

    def insert_password(self):
        report_step('Insert Password')