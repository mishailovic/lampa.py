import requests
from utils import settings
import json


def send(arguments):
    payload = {
        "clientId": settings.clientId,
        "accessToken": settings.accessToken,
        "data": json.dumps(arguments),
    }

    url = (
        "https://"
        + settings.region
        + ".openapp.io.mi.com/openapp/device/rpc/"
        + str(settings.deviceId)
    )  # shitcode, I know

    requests.post(
        url,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data=payload,
    )
