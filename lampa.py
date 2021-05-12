import json
from utils import datasender
from utils import settings


def toggle(arguments):
    if arguments == "on":
        params = "on"
    elif arguments == "off":
        params = "off"
    else:
        return 'Arguments are incorrect, only "on" and "off" is possible'

    json_data = {
        "did": settings.deviceId,
        "id": "1",
        "method": "set_power",
        "params": [params],
    }

    datasender.send(json_data)


def color(red, green, blue, effect="smooth", duration=500):
    rgb = (red * 65536) + (green * 256) + blue

    json_data = {
        "did": settings.deviceId,
        "id": "1",
        "method": "set_rgb",
        "params": [rgb, effect, duration],
    }

    datasender.send(json_data)
