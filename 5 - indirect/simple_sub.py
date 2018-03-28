#import library mqtt
import paho.mqtt.client as mqtt_client

#inisiasi client sebagai subcriber
#tidak boleh ada client id yg sama dalam 1 broker
#client() disi random oleh broker, bisa diisi sebagai ID
sub = mqtt_client.Client()

#koneksikan ke broker
sub.connect("127.0.0.1", 1883)

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
