import requests
import json

with open("settings/settings.json") as settings:
    data = json.loads(settings.read())


def send(device, arguments):
    with open(f"settings/devices/{device}.json") as settings:
        device_data = json.loads(settings.read())

    payload = {
        "clientId": data["clientId"],
        "accessToken": data["accessToken"],
        "data": json.dumps(arguments),
    }

    url = f"https://{data['region']}.openapp.io.mi.com/openapp/device/rpc/{str(device_data['did'])}"

    requests.post(
        url,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data=payload,
    )
