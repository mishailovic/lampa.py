from utils import login

client_id = 2882303761517308695
client_secret = "OrwZHJ/drEXakH1LsfwwqQ=="
creds = open("utils/settings.py")

data = login.get_token(client_id, client_secret)

print("Your access token is: " + data["access_token"])
