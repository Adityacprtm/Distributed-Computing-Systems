#import socket
import socket

#inisiasi objek
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#kirim req koneksi ke server
tcp_sock.connect(("127.0.0.1", 6667))

#kirim data
data = input('masukan angka: ')
tcp_sock.send( data.encode('utf-8'))

#baca data yg dikirim balik oelh serer
data = tcp_sock.recv(100)
data = data.decode('utf-8')
print(data)

tcp_sock.close
