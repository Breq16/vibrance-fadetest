import os
import threading
import logging

from flask import Flask, redirect
import vibrance

manager = vibrance.Manager()
manager.addScript("fadetest.py")
manager.chooseScript(manager.scripts["Fadetest"])

manager.connect(os.environ.get("RELAY_IP"), os.environ.get("RELAY_PSK"))
logging.getLogger("vibrance.controller.tolerant_socket").setLevel(logging.INFO)

app = Flask(__name__)


@app.route("/")
def index():
    return redirect("https://breq.dev/demos/vibrance/landing.html"
                    "?host=vibrance.breq.dev")


managerThread = threading.Thread(target=manager.run)
managerThread.start()

if __name__ == "__main__":
    app.run()
