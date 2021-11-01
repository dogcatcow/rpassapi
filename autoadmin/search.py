import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert

class SearchEngine(ChromeDriverManager):

    def __init__(self,
                 options=webdriver.ChromeOptions()):
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        # options.add_argument('--headless')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.wait = WebDriverWait(self.driver, 10)
        self.da = Alert(self.driver)
    def get_element(self, identify_method, identifier):
        element = None
        try:
            element = self.wait.until(
                EC.presence_of_element_located(
                    (identify_method, identifier)
                )
            )
        except TimeoutException:
            print("time out!!")
        finally:
            return element

    def change(self, list):
        da = Alert(self.driver)
        user_id = list[0]
        prev_pwd = list[1]

        self.driver.get("http://sample.population2d3fsz.com/")
        elem = self.get_element(By.ID, "user_id")
        elem.send_keys(list[0])
        elem = self.get_element(By.ID, "pwd")
        elem.send_keys(prev_pwd)
        elem = self.get_element(By.ID, "login-btn")
        elem.click()
        elem = self.get_element(By.ID, "login-btn")
        elem.click()
        elem = self.get_element(By.ID, "view_menu_button")
        elem.click()
        elem = self.get_element(By.LINK_TEXT, "화면권한관리")
        elem.click()
        elem = self.get_element(By.LINK_TEXT, "사용자관리")
        elem.click()
        elem = self.get_element(By.ID, "content_frame")
        self.driver.switch_to.frame(elem)
        elem = self.get_element(By.ID, "userInput")
        print("userinputt detected")
        elem.send_keys(user_id)
        elem = self.get_element(By.ID, "schBtn")
        print("schBtn DETECTED")
        elem.click()
        header_cell = self.get_element(By.XPATH, '//*[@id="userGridView"]/div/div[1]/div/div[1]/div[4]/div[4]/table/tbody/tr/td/div')
        print("userGridView DETECTED")
        #시차 발생부분
        time.sleep(3)
        header_cell.click()

        elem = self.get_element(By.ID, "resetPwdBtn")
        elem.click()
        # 시차 발생부분? 측정전

        da.accept()

