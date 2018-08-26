import paho.mqtt.client as mqtt_client
import time
import datetime
import random
import json

def on_publish(client, userdata, mid):
    print("mid: " + str(mid))

def imaginary_sensors():
    timestamp = datetime.datetime.now().strftime('%H:%M:%S')
    day_list = ["morn", "noon", "night"]
    temp = random.randint(10, 30)
    ph = random.randint(0, 14)
    hum = abs(temp*(temp/2)-500)
    day = day_list[1 if hum <= 150 else 0 if (hum > 150 and hum < 250) else 2]
    data = {
        "timestamp": timestamp,
        "temp": temp,
        "ph": ph,
        "hum": hum,
        "day": day
    }
    print(json.dumps(data))
    return json.dumps(data)

if __name__ == '__main__':
    pub = mqtt_client.Client()
    pub.on_publih = on_publish
    pub.connect("127.0.0.1", 1883)
    pub.loop_start()

    while True:
        i = 0
        while i < 1:
            (rc, mid) = pub.publish("/sensor/", imaginary_sensors(), qos=1)
            i += 1
        time.sleep(5)
