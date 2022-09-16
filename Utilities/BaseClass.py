import inspect
import logging

import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import AllureReports
from PageObjects.LoginPage import LoginPage
from PageObjects.Report import report_step
from TestData.DataSet import DataSet


@pytest.mark.usefixtures("setup")
class BaseClass:
    @allure.severity(allure.severity_level.BLOCKER)
    def LoginEmail(self):
        self.driver.implicitly_wait(10)
        loginpage=LoginPage(self.driver)
        loginpage.getEmail().send_keys(DataSet.Login_data[0])
        loginpage.getPassword().send_keys(DataSet.Login_data[1])
        loginpage.getSignInButton().click()
        Bs=loginpage.getBSText().text
        # assert "BOLDORY USERS" in BS
        url = self.driver.current_url
        assert "home" in url
        with allure.step('Do Login'):
            loginpage.go_to_login_page()
            loginpage.insert_user_name()
            loginpage.insert_password()

    def VerifylinkPresence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, text)))

    def getlogger(self):
        loggerName=inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        FileHandler = logging.FileHandler('Logfile.log')  # file handler is the location of parent
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        FileHandler.setFormatter(formatter)
        logger.addHandler(FileHandler)  # another class called file handler need to send object to this class
        logger.setLevel(logging.DEBUG)
        return logger