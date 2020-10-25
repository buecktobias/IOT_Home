from selenium import webdriver
from selenium.webdriver import ActionChains

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

action = ActionChains(browser)


def down_living_room_small():
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


if __name__ == '__main__':
    down_living_room_small()