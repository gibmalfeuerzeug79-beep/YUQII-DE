from pypresence import Presence
import requests
import time

CLIENT_ID = "1478716804636606627"
CONFIG_URL = "https://yuqiide.app/config"

RPC = Presence(CLIENT_ID)
RPC.connect()

print("Rich Presence gestartet")

while True:
    try:
        data = requests.get(CONFIG_URL).json()

        RPC.update(
            details=data["details"],
            state=data["state"],
            large_image=data["large_image"],
            large_text=data["large_text"],
            start=time.time()
        )

    except Exception as e:
        print("Fehler:", e)

    time.sleep(30)
