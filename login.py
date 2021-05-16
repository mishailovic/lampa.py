from utils import login
import json
import requests

client_id = 2882303761517308695
client_secret = "OrwZHJ/drEXakH1LsfwwqQ=="

data = login.get_token(client_id, client_secret)

settings = {"clientId": client_id, "accessToken": data["access_token"], "region": "de"}
with open("settings/settings.json", "w") as write_file:
    json.dump(settings, write_file)

payload = {
    "clientId": client_id,
    "accessToken": data["access_token"],
}

url = "https://de.openapp.io.mi.com/openapp/user/device_list"

r = requests.post(
    url,
    headers={"Content-Type": "application/x-www-form-urlencoded"},
    data=payload,
)

list_id = []
devices_json = json.loads(r.text)

for x in devices_json["result"]["list"]:
    lamps = {"did": x["did"], "name": x["name"], "model": x["model"], "mac": x["mac"]}

    with open(f'settings/devices/{x["name"]}.json', "w") as write_file:
        json.dump(lamps, write_file)
