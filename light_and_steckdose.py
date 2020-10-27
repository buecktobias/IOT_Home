import requests
import time

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