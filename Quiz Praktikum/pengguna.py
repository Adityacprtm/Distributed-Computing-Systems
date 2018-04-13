#Import xmlrpc client
import xmlrpc.client

# Koneksikan ke server RPC
proxy = xmlrpc.client.ServerProxy("http://127.0.0.1:7778/")

# Panggil fungsinya
sensor = proxy.sensor()
print(sensor)
#sensorJenis = proxy.jenis_sensor('suhu')
#print(sensorJenis)
