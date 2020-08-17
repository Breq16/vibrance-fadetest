import os

import vibrance

manager = vibrance.Manager()
manager.addScript("fadetest.py")
manager.chooseScript(manager.scripts["Fadetest"])

manager.connect(os.environ.get("VIBRANCE_RELAY_IP"),
                os.environ.get("VIBRANCE_RELAY_PSK"))

manager.run()
