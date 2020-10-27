import threading
from flask import Flask
from flask import render_template, redirect
from rolladen import *
from light_and_steckdose import *
import requests
import time
app = Flask(__name__)

r = None
rolladen_loader = None

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
    global r, rolladen_loader
    if r is not None and not rolladen_loader.is_alive():
        r.down_living_room_big()
    return ""

@app.route("/rolladen_up/", methods=["POST", "GET"])
def rolladen_hoch():
    global r , rolladen_loader
    if r is not None and not rolladen_loader.is_alive():
        r.up_living_room_big()
    return ""

@app.route("/rolladen_stop/", methods=["POST", "GET"])
def rolladen_stop():
    global r , rolladen_loader
    if r is not None and not rolladen_loader.is_alive():
        r.stop_living_room()
    return ""

@app.route("/rolladen_loading/", methods=["POST", "GET"])
def is_rolladen_loaded():
    global rolladen_loader
    if rolladen_loader.is_alive():
        return "is still Loading"
    else:
        return "is ready!"

@app.route("/get_status_steckdose/")
def get_status_steckdose():
    r = str(requests.get("http://192.168.178.132/?m=1").content)
    if "ON" in r:
        return "ON"
    else:
        return "OFF"


def load_rolladen():
    global r
    r = Rolladen()


def initialize_website():
    global rolladen_loader
    rolladen_loader = threading.Thread(target=load_rolladen)
    rolladen_loader.start()


def run_website():
    raise(Exception("HAHAH ww"))
    initialize_website()
    print("Start website")
    app.run(host="0.0.0.0", port=5001)


if __name__ == '__main__':
    run_website()
    # app.run(host="0.0.0.0", port=5001)

