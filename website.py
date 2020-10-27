import threading
from flask import Flask
from flask import render_template, redirect
try:
    from rolladen import *
except Exception as e:
    print(e)
    from .rolladen import *
try:
    from light_and_steckdose import *
except Exception as e:
    print(e)
    from .light_and_steckdose import *
import requests

app = Flask(__name__)

r:Rolladen = None
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


@app.route("rolladen_big_living_room/down/", methods=["POST", "GET"])
def rolladen_big_living_room_down():
    global r, rolladen_loader
    if r is not None and not rolladen_loader.is_alive():
        r.rolladen_big_living_room_down()
    return ""

@app.route("rolladen_big_living_room/up/", methods=["POST", "GET"])
def rolladen_big_living_room_up():
    global r , rolladen_loader
    if r is not None and not rolladen_loader.is_alive():
        r.rolladen_big_living_room_up()
    return ""

@app.route("/rolladen_big_living_room/stop/", methods=["POST", "GET"])
def rolladen_big_living_room_stop():
    global r , rolladen_loader
    if r is not None and not rolladen_loader.is_alive():
        r.rolladen_big_living_room_stop()
    return ""

@app.route("/rolladen_big_living_room/loading/", methods=["POST", "GET"])
def is_rolladen_big_living_room_loaded():
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
    initialize_website()
    print("Start website")
    app.run(host="0.0.0.0", port=5001)


if __name__ == '__main__':
    run_website()
    # app.run(host="0.0.0.0", port=5001)
