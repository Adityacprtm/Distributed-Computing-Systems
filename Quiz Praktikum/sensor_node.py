import paho.mqtt.client as mqtt_client
import sys
import random

pub = mqtt_client.Client()
pub.connect("127.0.0.1", 1883)
jenis = sys.argv[1]

if jenis == "suhu":
    suhu = random.randint(-10,50)
    pub.publish("/sensor/suhu/", suhu)
elif jenis == "kelembaban":
    lembab = random.randint(-10, 50)
    pub.publish("/sensor/kelembaban/", lembab)
elif jenis == "co":
    co = random.randint(-10, 50)
    pub.publish("/sensor/co/", co)
else:
    print("Sensor tidak tersedia!")