#import socket
import socket

#inisiasi objek socket UDP IP4
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#IP 0.0.0.0 bisa di akses dari mana saja, sebaliknya IP tertentu + port tertentu
#mengikat IP / port yg di akses agar proses lain tidak menggunakannya
sock.bind( ("0.0.0.0", 6666) )

while True:
    #baca data yg diterima dari client, blocking
    data, client_address = sock.recvfrom(1000)
    print(data , "From " , client_address)
    angka = int(data)%2
    if angka == 0:
        #ubah data
        data = "OK - angka GENAP"
        #kirim ke client
        sock.sendto(data.encode('utf-8'), client_address)
    else:
        #ubah data
        data = "OK - angka GANJIL"
        #kirim ke client
        sock.sendto(data.encode('utf-8'), client_address)
