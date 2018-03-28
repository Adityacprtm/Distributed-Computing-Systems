import paho.mqtt.client as mqtt_client
from threading import Thread

dok = mqtt_client.Client()
dok.connect("127.0.0.1", 1883)

################# S U B S C R I B E #################
def handle_message(mqttc, obj, msg):
    print(msg)
    topic = msg.topic
    payload = msg.payload
    payload = payload.decode('ascii')
    print("Topik : " + topic + " || Payload : " + payload)

dok.on_message = handle_message

kdr_gula = input("Kadar Gula = ")
subs = "/kadar/gula/" + kdr_gula
dok.subscribe(subs)

dok.loop_forever()
#################################################

################# P U B L I S H #################
dok.publish("/kadar/gula/175", "Saran saya anda mati saja")
dok.publish("/kadar/gula/150", "Saran saya anda bunuh diri")
#################################################