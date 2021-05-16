import json
from utils import datasender


def toggle(device, arguments):

    json_data = {
        "method": "set_power",
        "params": [arguments],
    }

    datasender.send(device, json_data)


def color(device, red, green, blue, effect="smooth", duration=500):
    rgb = (red * 65536) + (green * 256) + blue

    json_data = {
        "method": "set_rgb",
        "params": [rgb, effect, duration],
    }

    datasender.send(device, json_data)


def brightness(device, brightness, effect="smooth", duration=500):

    json_data = {
        "method": "set_bright",
        "params": [brightness, effect, duration],
    }

    datasender.send(device, json_data)


def color_temp(device, ct_value, effect="smooth", duration=500):

    json_data = {
        "method": "set_ct_abx",
        "params": [ct_value, effect, duration],
    }

    datasender.send(device, json_data)
