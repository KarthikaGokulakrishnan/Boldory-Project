from selenium.webdriver.common.by import By


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