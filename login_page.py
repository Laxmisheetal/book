import time
from excel_library import read_locators
loc_file_path=r"C:\Users\LENOVO\Downloads\actitime_locators.xlsx"
login_sheet_name="login_objects"

class LoginPage:

        locators=read_locators(loc_file_path,login_sheet_name)
        print(locators)

        def __init__(self,driver):
                 self.driver=driver


        def enter_username(self,username):
            self.driver.find_element(*self.locators["username_txt"]).send_keys(username)
            time.sleep(2)

        def enter_password(self,password):
            self.driver.find_element(*self.locators["password_txt"]).send_keys(password)
            time.sleep(2)


        def click_login_btn(self):
            self.driver.find_element(*self.locators["login_btn"]).click()
            time.sleep(2)