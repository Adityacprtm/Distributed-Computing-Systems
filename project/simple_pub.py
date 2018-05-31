#import library mqtt
import paho.mqtt.client as mqtt_client
from time import sleep

broker = "m11.cloudmqtt.com"
port = 19671
usrname = "pcmzmruz"
password = "OS_6HVAJUFSq"
#inisiasi client sebagai publisher
#tidak boleh ada client id yg sama dalam 1 broker
#client() disi random oleh broker, bisa diisi sebagai ID
pub = mqtt_client.Client()
pub.username_pw_set(usrname, password)

#koneksikan ke broker, port default 1883
pub.connect(broker, port)

#publish message
while True:
    pub.publish("/sensor/suhu/3", "80")
    pub.publish("/sensor/co/1", "10")
    pub.publish("/sensor/co2/1", "20%")
    pub.publish("/sensor/co2/2", "5%")
    pub.publish("/sensor/co2/3", "100%")
    pub.publish("/rahasia/cur/8", "haha")
    pub.publish("/sensor/suhu/1", "30")
    pub.publish("/sensor/suhu/2", "25")
    sleep(20)
