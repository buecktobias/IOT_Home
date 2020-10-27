from flask import Flask
from flask import render_template, redirect
from rolladen import *
from light_and_steckdose import *
import requests
import time
app = Flask(__name__)


browser, action = get_browser_and_action()
devises = get_devises(browser, action)
browser = get_rolladen_big_living_room(browser, action)





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
    down_living_room_big(browser)
    return ""

@app.route("/get_status_steckdose/")
def get_status_steckdose():
    r = str(requests.get("http://192.168.178.132/?m=1").content)
    if "ON" in r:
        return "ON"
    else:
        return "OFF"


def run_website():
    app.run(host="0.0.0.0", port=5001)


if __name__ == '__main__':
    run_website()
    # app.run(host="0.0.0.0", port=5001)

