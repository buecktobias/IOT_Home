from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_browser_and_action():
    browser = None
    try:
        browser = webdriver.Firefox()
    except:
        try:
            browser = webdriver.Chrome()
        except:
            pass
        pass
    if browser is None:
        raise("No browser!")
    browser.implicitly_wait(3)
    action = ActionChains(browser)
    return browser, action


def get_rolladen_big(browser, action):
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
    rolladen_big = "devices1394"
    rolladen_big_button = browser.find_element_by_id(rolladen_big)
    action.move_to_element_with_offset(rolladen_big_button, 5, 5).click().perform()
    return browser


def down_living_room_big():
    browser, action = get_browser_and_action()
    browser = get_rolladen_big(browser, action)
    id_down = "/html/body/div[9]/div/div[3]/table/tbody/tr/td[2]/div/table/tbody/tr/td/table/tbody/tr[3]/td[5]/table/tbody/tr/td/table/tbody/tr/td[4]/table/tbody/tr[2]/td/table"
    wait = WebDriverWait(browser, 10)
    rolladen = wait.until(EC.element_to_be_clickable((By.XPATH, id_down)))
    rolladen.click()
    browser.close()