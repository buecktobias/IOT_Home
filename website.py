from flask import Flask
from flask import render_template, url_for, redirect
from rolladen import down_living_room_big
import requests
import time
app = Flask(__name__)

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

@app.route("/rolladen_living_room1/", methods=["POST"])
def rolladen_runter():
    down_living_room_big()
    return ""

@app.route("/get_status_steckdose/")
def get_status_steckdose():
    r = str(requests.get("http://192.168.178.132/?m=1").content)
    if "ON" in r:
        return "ON"
    else:
        return "OFF"


def run_website():
    """    #TODO try
    try:
        subprocess.call("sudo apt-get install Iceweasel", shell=True)
    except:
        pass"""
    app.run(host="0.0.0.0", port=5001)


if __name__ == '__main__':
    print("LOL")
    app.run(host="0.0.0.0", port=5001)

