import time

import pytest
from selenium.webdriver.common.by import By

from PageObjects.UserManagement import UserManagement
from TestData.DataSet import DataSet
from Utilities.BaseClass import BaseClass
import allure



@allure.severity(allure.severity_level.NORMAL)
class TestSearchUser(BaseClass):


    def objects(self):
        id = UserManagement(self.driver)
        return id
        # return UserManagement(self.driver)

    @allure.severity(allure.severity_level.MINOR)
    def test_SearchByUser(self):
        self.driver.implicitly_wait(10)
        log = self.getlogger()
        self.LoginEmail()
        self.objects().getSearchText().send_keys(DataSet.searchUserText)
        UserName = self.objects().getSearchList()
        log.info(len(UserName))
        for username in UserName:
            if username.text == "SANKAVI RS":
                assert username.text == "SANKAVI RS"
                break
        self.objects().getSearchText().clear()
        log.info("User Searched And verified Successfully")
        with allure.step('Do Search Using UserName'):
            self.objects().SearchUser()



    def test_SendNotification(self):
        log = self.getlogger()
        self.driver.implicitly_wait(10)
        self.objects().getdotIcon().click()
        self.objects().getmenuItem2().click()
        self.objects().getTextarea().send_keys(DataSet.MailContent)
        self.objects().getsendButton().click()
        time.sleep(0.5)
        msg=self.objects().getSnackMsg().text
        assert "Notification sent" in msg
        log.info(msg)
        log.info("Notification sent to the user Successfully")
        with allure.step('Do send the Notification'):
            self.objects().SendNotification()


    def test_SupendUser(self):
        log=self.getlogger()
        self.driver.implicitly_wait(10)
        self.objects().getdotIcon().click()
        self.objects().getmenuItem1().click()
        time.sleep(0.5)
        msg=self.objects().getSnackMsg().text
        assert "Suspended User." in msg
        log.info(msg)
        status=self.objects().getStatus().text
        assert status=="SUSPENDED"
        self.objects().getdotIcon().click()
        self.objects().getmenuItem1().click()
        time.sleep(0.5)
        msg = self.objects().getSnackMsg().text
        assert "Activated User." in msg
        log.info(msg)
        status = self.objects().getStatus().text
        assert status == "ACTIVE"
        log.info("User suspended and activated")
        with allure.step('Do suspend and activate user'):
            self.objects().SuspendUser()


    #
    def test_AddAdmin(self):
        log=self.getlogger()
        self.driver.implicitly_wait(10)
        self.objects().getTab().click()
        self.objects().getAddButton().click()
        self.objects().getFirstName().send_keys(DataSet.Addadmin[0])
        self.objects().getLastName().send_keys(DataSet.Addadmin[1])
        self.objects().getEmail().send_keys(DataSet.Addadmin[2])
        self.objects().getPassword().send_keys(DataSet.Addadmin[3])
        self.objects().getCreateButton().click()
        time.sleep(0.5)
        msg = self.objects().getSnackMsg().text
        assert msg== "Admin Created"
        log.info("Admin Added Successfully")
        with allure.step('Do Add Admin'):
            self.objects().AddAdmin()



    def test_SuspendAdmin(self):
        log = self.getlogger()
        self.driver.implicitly_wait(10)
        self.objects().getAdmindotIcon().click()
        self.objects().getAddadminMenuItem().click()
        time.sleep(0.5)
        msg=self.objects().getSnackMsg().text
        assert msg== "Suspended Admin."
        log.info(msg)
        status=self.objects().getAdminStatus().text
        assert status=="SUSPENDED"
        log.info(status)
        self.objects().getAdmindotIcon().click()
        self.objects().getAddadminMenuItem().click()
        time.sleep(0.5)
        msg = self.objects().getSnackMsg().text
        log.info(msg)
        assert msg == "Activated Admin."
        status = self.objects().getAdminStatus().text
        log.info(status)
        assert status == "ACTIVE"
        log.info("Admin suspended and activated")
        with allure.step('Do Suspend and Activate admin'):
            self.objects().SuspendAdmin()








