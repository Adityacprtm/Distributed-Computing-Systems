#import library mqtt
import paho.mqtt.client as mqtt_client

#inisiasi client sebagai publisher
#tidak boleh ada client id yg sama dalam 1 broker
#client() disi random oleh broker, bisa diisi sebagai ID
pub = mqtt_client.Client()

#koneksikan ke broker, port default 1883
pub.connect("127.0.0.1", 1883)

#publish message
pub.publish("/sensor/suhu/1", "30")
pub.publish("/sensor/suhu/2", "25")
pub.publish("/sensor/co/1", "20%")
pub.publish("/sensor/co/2", "5%")
