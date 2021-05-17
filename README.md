# lampa.py
Simple python lib to interact with Xiaomi lamps [WIP]


# Before installing:
To configure all your lamps, you need to download Yeelight app from [App Store](https://apps.apple.com/app/yeelight/id977125608) or [Google Play](https://play.google.com/store/apps/details?id=com.yeelight.cherry). When you will be asked about region, choose Frankfurt.
<details>
  <summary>Region</summary>
  
   ![region](https://mishailovic.github.io/assets/Screenshot_20210517-091803.png)
 
</details> 

(This is a region with a minimum latency, and unfortunately I also did not understand how to find out which region the user is in.) 

Add all your lamps, and most importantly, give them recognizable short names without special characters, so it will be easier for you to control the lamps in the future.

<details>
  <summary>Lamp naming example</summary>
  
   ![region](https://mishailovic.github.io/assets/Screenshot_20210517-111018.png)
 
</details>

Well done! You are ready to install the library and you can uninstall yeelight if you don't need it.

# Installation:

```
git clone https://github.com/mishailovic/lampa.py
cd lampa.py
pip3 install -r requirements.txt
```

# Logging in and getting information ablout lamps:

```
python3 login.py
```

This script will automatically receive all your lamp's credentials, just follow the instructions in the terminal.


# Examle usage:

```
>>> import lampa
>>> lampa.toggle("bedside", "on") # ("bedside" is a name of my lamp which i configured in yeelight app.)
```

*lamp turns on, hooray!*

# Docs:

Comming soon!


