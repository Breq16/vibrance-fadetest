import math
import time

import vibrance

api = vibrance.Interface("Fadetest")


def getColor(radians):
    red = 0x80 + int(0x79*math.sin(radians))
    green = 0x80 + int(0x79*math.sin(radians+math.pi*2/3))
    blue = 0x80 + int(0x79*math.sin(radians+math.pi*4/3))
    return f"{format(red, '02x')}{format(green, '02x')}{format(blue, '02x')}"


@api.onTelemetry
def onTelemetry(telemetry):
    print(telemetry)


frame = 0


@api.loop
def mainloop():
    global frame
    api.clear()
    for i in range(20):
        api.add(0, getColor(frame/50), delay=i*50)
        api.add(1, getColor(frame/50+math.pi*1/3), delay=i*50)
        api.add(2, getColor(frame/50+math.pi*2/3), delay=i*50)
        api.add(3, getColor(frame/50+math.pi), delay=i*50)
        api.add(4, getColor(frame/50+math.pi*4/3), delay=i*50)
        api.add(5, getColor(frame/50+math.pi*5/3), delay=i*50)
        frame += 1
    ts = time.time()
    time.sleep(1 + ts - time.time())
