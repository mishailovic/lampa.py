# lampa.py
Simple python lib to interact with Xiaomi lamps [WIP]

Tutorial for getting variables:

• You need rooted device, until I figure out how to get token values and device ID without root.

• Download yeelight app from google play, and connect your lamp. If yeelight will ask you about server location choose east Europe.

• Go to /data/data/com.yeelight.cherry/shared_perfs/acces.token.xml and copy value which starts with “V3”. This is your accessToken, save it.

• Go to /data/data/com.yeelight.cherry/shared_perfs/mipush_account.xml and copy value from string “app_id”. This is deviceId, you also need to save it somewhere.

• Find the device.db in /data/data/ com.yeelight.cherry/databases and copy the device id value, this is deviceId.

examle usage:

```
>>> import lampa
>>> lampa.toggle("on")
```

*lamp turns on, hooray!*


