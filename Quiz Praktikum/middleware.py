import paho.mqtt.client as mqtt_client
import xmlrpc.server
import json
from threading import Thread

with open('data.json') as json_data:
    data = json.load(json_data)

server = xmlrpc.server.SimpleXMLRPCServer(("0.0.0.0", 7778))

def handle_publisher(conn):
    def handle_message(mqttc, obj, msg):
        topic = msg.topic
        payload = msg.payload
        payload = payload.decode('ascii')
        data_split = topic.split("/")
        jenis = data_split[2]
        data_baru = {
            jenis: payload
        }
        data.append(data_baru)
        with open('data.json', 'w') as f:
            json.dump(data, f)
        print("Topik : " + topic + " || Payload : " + payload)

    conn.subscribe("/sensor/#")
    conn.on_message = handle_message
    conn.loop_forever()

def get_all():
    return data

def get_sensor(jenis):
    for i in range(0, len(data)):
        if jenis == data[i][jenis]:
            return data[i]

server.register_function(get_all, 'sensor')
server.register_function(get_sensor, 'jenis_sensor')

server.serve_forever()

while True:
    sub = mqtt_client.Client()
    conn = sub.connect("127.0.0.1", 1883)
    t = Thread(target=handle_publisher, args=(conn,))
    t.start()
