from selenium import webdriver
import time
import unittest
from pages.loginpage import LoginPage
from pages.homepage import HomePage

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/Pijush/PycharmProjects/Page Object Model/webdriver/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        time.sleep(3)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        time.sleep(3)
        homepage.click_welcome()
        time.sleep(2)
        homepage.click_logout()

        #self.driver.get("https://opensource-demo.orangehrmlive.com/")
        # self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        # time.sleep(2)
        # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        # time.sleep(2)
        # self.driver.find_element_by_id("btnLogin").click()
        # self.driver.find_element_by_id("welcome").click()
        # time.sleep(4)
        # self.driver.find_element_by_link_text("Logout").click()

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")