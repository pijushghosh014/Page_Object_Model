class HomePage():
    def __init__(self, driver):                    #creat a constructor
        self.driver = driver

        self.welcome_id = "welcome"
        self.logout_linktext = "Logout"

    def click_welcome(self):
         self.driver.find_element_by_id(self.welcome_id).click()

    def click_logout(self):
         self.driver.find_element_by_link_text(self.logout_linktext).click()
