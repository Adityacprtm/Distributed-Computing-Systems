from pymongo import MongoClient
import paho.mqtt.client as mqtt_cient
import time
import json
import struct
import socket
import datetime

client = MongoClient('mongodb://127.0.0.1:27017/')
db = client.iot_db

def on_subscribe(client, userdata, mid, granted_ops):
    print("subscribed: " + str(mid) + " " + str(granted_ops))

def on_message(mqtt, obj, msg):
    topic = msg.topic
    payload = msg.payload
    payload = payload.decode('ascii')
    data.append(json.loads(payload))
    send_msg(json.dumps(data))
    data[:] = []

def send_msg(msg):
    if(msg != None):
        print("Receive Data")
        dataJson = json.loads(msg)
        print("Send to MongoDB")
        db.sensor.insert_many(dataJson)
    # sebagai gateway
    #rcv_ip = "127.0.0.1"
    #rcv_port = 6667

    #msg = struct.pack('<I', len(msg)) + msg
    # Koneksi ke Receiver
    #tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #tcp_sock.connect((rcv_ip, rcv_port))
    #tcp_sock.send(msg)
    #tcp_sock.close()

if __name__ == "__main__":
    data = []
    # sebagai subscriber
    broker_ip = "127.0.0.1"
    broker_port = 1883
    sub = mqtt_cient.Client(clean_session=True)
    sub.on_subscribe = on_subscribe
    sub.on_message = on_message
    print("Sending Data")
    sub.connect(broker_ip, broker_port)
    sub.subscribe("/sensor/#", 1)
    sub.loop_forever()
