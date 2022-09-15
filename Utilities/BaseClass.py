import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.LoginPage import LoginPage
from TestData.DataSet import DataSet


@pytest.mark.usefixtures("setup")
class BaseClass:

    def LoginEmail(self):
        self.driver.implicitly_wait(10)
        loginpage=LoginPage(self.driver)
        DataSet.Login_data
        loginpage.getEmail().send_keys(DataSet.Login_data[0])
        loginpage.getPassword().send_keys(DataSet.Login_data[1])
        loginpage.getSignInButton().click()
        Bs=loginpage.getBSText().text
        # assert "BOLDORY USERS" in BS
        url = self.driver.current_url
        assert "home" in url

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