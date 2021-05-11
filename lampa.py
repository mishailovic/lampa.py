import requests
import configparser
import json

def toggle(arguments):
    
    config = configparser.ConfigParser()
    config.read("settings.ini")
    
    json_data = {
        "did": config["Variables"]["deviceId"],
        "id": "1",
        "method": "set_power",
        "params": [
            arguments
        ]    
    }

    payload = {
        "clientId": config["Variables"]["clientId"],
        "accessToken": config["Variables"]["accessToken"],
        "data": json.dumps(json_data),
    }

    region = config["Variables"]["region"]

    url = (
        "https://"
        + region
        + ".openapp.io.mi.com/openapp/device/rpc/"
        + str(config["Variables"]["deviceId"])
    )  # shitcode, I know

    requests.post(
        url,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data=payload,
    )
