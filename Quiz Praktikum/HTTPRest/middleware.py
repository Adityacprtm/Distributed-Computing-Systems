import socket
import threading
from flask import Flask, request
import paho.mqtt.client as mqtt_client
import json

app = Flask("Web App sensor")

sub = mqtt_client.Client()

sub.connect("127.0.0.1", 1883)

list_data_sensor = {}

def handle_msg(mqttc, obj, msg):
    topic = msg.topic
    payload = msg.payload
    payload = payload.decode('utf-8')
    print(payload)
    data_sensor = json.loads(payload)
    jenis_sensor = data_sensor["jenis_sensor"]
    if jenis_sensor in list_data_sensor:
        list_data_sensor[jenis_sensor].append(data_sensor["nilai"])
    else:
        list_data_sensor[jenis_sensor] = []
        list_data_sensor[jenis_sensor].append(data_sensor["nilai"])

def handle_subscriber():
    sub.on_message = handle_msg
    sub.subscribe("/sensor/#")
    sub.loop_forever()

t = threading.Thread(target=handle_subscriber)
t.start()

@app.route('/sensor', methods=['GET'])
def get_sensor():
    json_sensor = json.dumps(list_data_sensor)
    return json_sensor

@app.route('/sensor/<string:jenis_sensor>', methods=['GET'])
def get_sensor_name(jenis_sensor):
    if jenis_sensor in list_data_sensor:
        msg = json.dumps(list_data_sensor[jenis_sensor])
    else:
        msg = "Sensor tidak tersedia"
    return msg

print("Server HTTP run di port 7777")
app.run(port=7777)
# To Do : Bagian Server
