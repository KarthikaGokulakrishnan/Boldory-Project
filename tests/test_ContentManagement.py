import time

import allure
from selenium.webdriver.common.by import By

from PageObjects.ContentManagement import ContentManagement
from Utilities.BaseClass import BaseClass
from TestData.DataSet import DataSet


class TestContentManagement(BaseClass):
    def objects(self):
        id = ContentManagement(self.driver)
        return id
    def test_ViewRequest(self):
        self.driver.implicitly_wait(10)
        log = self.getlogger()
        self.LoginEmail()
        self.objects().getcontentmanagementmenu().click()
        SN=self.objects().getscriptName()
        log.info(len(SN))
        for ScriptName in SN:
            log.info(ScriptName.text)
            if ScriptName.text=="Surface":
                log.info(ScriptName.text)
                log.info("Script Surface was found out from the List")
                break
        log.info("List of Scripts are viewed successfully")
        with allure.step('View List of Scripts'):
            self.objects().ListOfScripts()

    def test_RejectRequest(self):
        self.driver.implicitly_wait(10)
        log = self.getlogger()
        self.objects().getapprovedTab().click()
        self.objects().getsearchBar().send_keys(DataSet.scriptname)
        SN = self.objects().getscriptName()
        log.info(len(SN))
        for Scriptname in SN:
            if Scriptname.text == "Mulan":
                assert Scriptname.text == "Mulan"
                break
        self.objects().getdotIcon().click()
        self.objects().getmenuItem().click()
        self.objects().getrejectionReason().send_keys(DataSet.rejectionReason)
        self.objects().getsubmitButton().click()
        time.sleep(0.5)
        msg=self.objects().getmsg().text
        assert "Rejected Content" in msg
        log.info("Script Request are rejected successfully")
        with allure.step('Reject the script request'):
            self.objects().RejectScript()

    def test_ApproveRequest(self):
        self.driver.implicitly_wait(10)
        log = self.getlogger()
        self.objects().getrejectedTab().click()
        self.objects().getsearchBar().send_keys(DataSet.scriptname)
        self.objects().getdotIcon().click()
        self.objects().getmenuItem().click()
        time.sleep(0.5)
        msg=self.objects().getmsg().text
        assert "Approved content" in msg
        log.info("Script Request are Approved successfully")
        with allure.step('Approve the script request'):
            self.objects().ApproveScript()

    def test_category(self):
        self.driver.implicitly_wait(10)
        log = self.getlogger()
        self.objects().getcategoryTab().click()
        self.objects().getaddCategory().click()
        self.objects().getcategoryName().send_keys(DataSet.categoryname)
        self.objects().getimgupload().send_keys(DataSet.imgPath)
        self.objects().getaddButton().click()
        time.sleep(2)
        msg = self.objects().getmsg().text
        assert "Category created" in msg
        self.objects().getdeleteIcon().click()
        self.objects().getsuspendButton().click()
        time.sleep(0.5)
        msg1 = self.objects().getmsg().text
        assert "Category suspended" in msg1
        log.info("New category added and suspended sucessfully")
        with allure.step('Add category and suspend category'):
            self.objects().Addcategory()


