from flask import Flask
from flask import render_template, url_for, redirect

import requests
import time
app = Flask(__name__)
try:
    from selenium import webdriver
    from selenium.webdriver import ActionChains
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
except Exception as e:
    pass

def get_browser_and_action():
    browser = None
    try:
        browser = webdriver.Firefox()
    except Exception:
        try:
            browser = webdriver.Chrome()
        except Exception:
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


address_light = "http://192.168.178.131/?m=1&o=1"
address_steckdose = "http://192.168.178.132/?m=1&o=1"

WEBSITE_LIGHT = "http://192.168.178.131/"
WEBSITE_STECKDOSE = "http://192.168.178.132"


def toggle_steckdose():
    requests.get(address_steckdose)

def switch_light():
    requests.get(address_light)


def blink_light(time_wait):
    switch_light()  # ON
    time.sleep(time_wait)
    switch_light()  # OUT
    time.sleep(time_wait)


def blink_light_multiple_times(time_wait, amount):
    for i in range(amount):
        blink_light(time_wait)


@app.route("/terassen_licht/")
def terassenlicht_website():
    return redirect(WEBSITE_LIGHT)

@app.route("/toggle_steckdose/", methods=["POST"])
def toggle_steckdose_url():
    toggle_steckdose()
    return ""


@app.route("/toggle_light/", methods=["POST"])
def toggle_light():
    switch_light()
    return ""

@app.route("/steckdose/")
def steckdose_website():
    return redirect(WEBSITE_STECKDOSE)


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/get_status_light/")
def get_status_light():
    r = str(requests.get("http://192.168.178.131/?m=1").content)
    if "ON" in r:
        return "ON"
    else:
        return "OFF"

@app.route("/rolladen/", methods=["POST", "GET"])
def rolladen_runter():
    try:
        down_living_room_big()
    except Exception as e:
        return str(e)
    return ""

@app.route("/get_status_steckdose/")
def get_status_steckdose():
    r = str(requests.get("http://192.168.178.132/?m=1").content)
    if "ON" in r:
        return "ON"
    else:
        return "OFF"


def run_website():
    import subprocess
    #TODO try
    try:
        subprocess.call("sudo apt-get install Iceweasel", shell=True)
    except Exception:
        pass
    app.run(host="0.0.0.0", port=5001)


if __name__ == '__main__':
    run_website()
    # app.run(host="0.0.0.0", port=5001)

