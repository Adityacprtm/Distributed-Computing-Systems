from pymongo import MongoClient
from threading import Thread
import socket
import sys
import struct
import json
import datetime

client = MongoClient('mongodb://192.168.56.121:27017/')
db = client.iot_db

def handle_thread(conn):
    try:
        data = rcv_msg(conn)
        if(data != None):
            data = data.decode('ascii')
            print("Receive Data")
            dataJson = json.loads(data)
            print("Send to MongoDB")
            db.sensor.insert_many(dataJson)
    except (socket.error):
        conn.close()
        print("Connection Closed by Peer")
    except:
        print("Unexpected error:", sys.exc_info())
        conn.close()

def rcv_msg(conn):
    #baca ukuran data int = 4byte
    size = conn.recv(4)
    size = struct.unpack("<I", size)[0]
    #baca data
    data = conn.recv(size)
    #decode
    return data

if __name__ == '__main__':
    # Receiver
    rcv_ip = "0.0.0.0"
    rcv_port = 6667

    # mongoDB
    #mongo_ip = "127.0.0.1"
    #mongo_port = 27017

    tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_sock.bind((rcv_ip, rcv_port))
    tcp_sock.listen(10)

    print('Listening at', tcp_sock.getsockname())
    print("Press Crtl+c to exit...")

    while True:
        #terima req keneksi
        conn, client_address = tcp_sock.accept()

        #buat thread baru untuk setiap permintaan koneksi
        t = Thread(target=handle_thread, args=(conn,))

        #start thread
        t.start()
