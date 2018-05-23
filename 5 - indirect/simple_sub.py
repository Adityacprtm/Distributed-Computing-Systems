#import library mqtt
import paho.mqtt.client as mqtt_client

broker = "m11.cloudmqtt.com"
port = 19671
usrname = "pcmzmruz"
password = "OS_6HVAJUFSq"
#inisiasi client sebagai publisher
#tidak boleh ada client id yg sama dalam 1 broker
#client() disi random oleh broker, bisa diisi sebagai ID
sub = mqtt_client.Client()
sub.username_pw_set(usrname, password)

#koneksikan ke broker, port default 1883
sub.connect(broker, port)

#fungsi untuk handle msg yg baru masuk
def handle_message(mqttc, obj, msg):
    #dapatkan topik dan payload
    topic = msg.topic
    payload = msg.payload
    payload = payload.decode('ascii')
    #cetak ke layar
    print("Topik : " + topic + " || Payload : " + payload)

#daftarkan fungsi untuk event on_message
sub.on_message = handle_message

#subcribe ke seuah topik
sub.subscribe("/sensor/#")
sub.subscribe("/rahasia/#")

#loop forever agar sub tidak mati
sub.loop_forever()
