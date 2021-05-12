import requests, json, webbrowser


def get_token(client_id, client_secret):
    print(
        "Mi Account OAuth authorization page should open right now, if that didnt happen, open the link below in your browser."
    )
    print(
        f"https://account.xiaomi.com/oauth2/authorize?client_id={client_id}&response_type=code&redirect_uri=http://www.mi.com"
    )
    print("")

    webbrowser.open(
        f"https://account.xiaomi.com/oauth2/authorize?client_id={client_id}&response_type=code&redirect_uri=http://www.mi.com"
    )

    print(
        "After authorization you should see something like https://www.mi.com/ru/?code=KSMOSCLOUDSRV_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX in your URL bar"
    )
    print(
        "You should copy and paste the code right here, here's how a valid code should look like: KSMOSCLOUDSRV_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    )
    print("")
    code = input("Enter the code: ")

    with requests.get(
        "https://account.xiaomi.com/oauth2/token",
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4495.0 Safari/537.36"
        },
        params={
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "authorization_code",
            "redirect_uri": "http://www.mi.com",
            "code": code,
        },
    ) as res:
        return json.loads(res.text.replace("&&&START&&&", ""))
