import http.client
import json

ip_server = "127.0.0.1"
port_server = 7777

def get_sensor():
    conn = http.client.HTTPConnection(ip_server, port=port_server)
    conn.request('GET', '/sensor')
    response = conn.getresponse().read()
    print(response.decode('utf-8'))

get_sensor()