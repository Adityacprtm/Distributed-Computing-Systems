import paho.mqtt.client as mqtt_client
from threading import Thread

pas = mqtt_client.Client()
pas.connect("127.0.0.1", 1883)

################# S U B S C R I B E #################
def handle_message(mqttc, obj, msg):
    print(msg)
    topic = msg.topic
    payload = msg.payload
    payload = payload.decode('ascii')
    print("Topik : " + topic + " || Payload : " + payload)

pas.on_message = handle_message

kdr_gula = input("Kadar Gula = ")
subs = "/kadar/gula/" + kdr_gula
pas.subscribe(subs)

pas.loop_forever()
#################################################

################# P U B L I S H #################
pas.publish("/kadar/gula/175", "Saran saya anda mati saja")
pas.publish("/kadar/gula/150", "Saran saya anda bunuh diri")
#################################################
