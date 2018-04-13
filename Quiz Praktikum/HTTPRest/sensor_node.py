import paho.mqtt.client as mqtt_client
from random import randint
from time import sleep
import json
import sys

pub = mqtt_client.Client()

pub.connect("127.0.0.1", 1883)

jenis_sensor = sys.argv[1]

for i in range(0,100):
    suhu = randint(20,35)
    data_sensor = {
        "jenis_sensor" : jenis_sensor,
        "id" : "filkom",
        "nilai" : suhu
    }
    print("kirim data sensor " + jenis_sensor + " " + str(suhu))
    data_sensor = json.dumps(data_sensor)
    pub.publish("/sensor/" + jenis_sensor, data_sensor)
    sleep(2)