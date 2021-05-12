import requests
from utils import settings
import json


def send(arguments):
    payload = {
        "clientId": settings.clientId,
        "accessToken": settings.accessToken,
        "data": json.dumps(arguments),
    }

    url = f"https://{settings.region}.openapp.io.mi.com/openapp/device/rpc/{str(settings.deviceId)}"

    requests.post(
        url,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data=payload,
    )
