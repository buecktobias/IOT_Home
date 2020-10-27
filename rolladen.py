from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options


class Rolladen():
    def __init__(self):
        self.browser, self.action = self.get_browser_and_action()
        self.rolladen_big_browser = self.initialize_rolladen_living_room()
        print("Initialized Rolladen")

    def initialize_rolladen_living_room(self):
        devises_browser = self.get_devises(self.browser, self.action)
        rolladen_big_browser = self.get_rolladen_big_living_room(devises_browser, self.action)
        return rolladen_big_browser

    def get_browser_and_action(self):
        try:
            options = Options()
            options.headless = True
            browser = webdriver.Firefox(options=options)
        except Exception as e:
            print(e)
            browser = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
        browser.implicitly_wait(3)
        action = ActionChains(browser)
        return browser, action

    def get_devises(self, browser, action):
        login_url = "http://192.168.178.23/login.htm"
        browser.get(login_url)
        admin_button = "/html/body/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[1]/table/tbody/tr/td/div"
        browser.find_element_by_xpath(admin_button).click()
        login = "/html/body/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]/form/table/tbody/tr[5]/td/div"
        browser.find_element_by_xpath(login).click()
        status_and_control = "/html/body/div[9]/div/div[2]/div[2]/div[1]"
        action.move_to_element(browser.find_element_by_xpath(status_and_control)).perform()
        devices = "/html/body/div[9]/div/div[2]/div[2]/div[2]/div/div[3]"
        browser.find_element_by_xpath(devices).click()
        return browser

    def get_rolladen_big_living_room(self, browser, action):
        rolladen_big = "devices1394"
        rolladen_big_button = browser.find_element_by_id(rolladen_big)
        action.move_to_element_with_offset(rolladen_big_button, 5, 5).click().perform()
        return browser

    def down_living_room_big(self):
        browser = self.rolladen_big_browser
        id_down = "/html/body/div[9]/div/div[3]/table/tbody/tr/td[2]/div/table/tbody/tr/td/table/tbody/tr[3]/td[5]/table/tbody/tr/td/table/tbody/tr/td[4]/table/tbody/tr[2]/td/table"
        wait = WebDriverWait(browser, 10)
        rolladen = wait.until(EC.element_to_be_clickable((By.XPATH, id_down)))
        rolladen.click()

    def up_living_room_big(self):
        browser = self.rolladen_big_browser
        id_up = "/html/body/div[9]/div/div[3]/table/tbody/tr/td[2]/div/table/tbody/tr/td/table/tbody/tr[3]/td[5]/table/tbody/tr/td/table/tbody/tr/td[4]/table/tbody/tr[1]/td/table"
        wait = WebDriverWait(browser, 10)
        rolladen = wait.until(EC.element_to_be_clickable((By.XPATH, id_up)))
        rolladen.click()

    def stop_living_room(self):
        browser = self.rolladen_big_browser
        id_stop = "/html/body/div[9]/div/div[3]/table/tbody/tr/td[2]/div/table/tbody/tr/td/table/tbody/tr[3]/td[5]/table/tbody/tr/td/table/tbody/tr/td[3]/div"
        wait = WebDriverWait(browser, 10)
        rolladen = wait.until(EC.element_to_be_clickable((By.XPATH, id_stop)))
        rolladen.click()
