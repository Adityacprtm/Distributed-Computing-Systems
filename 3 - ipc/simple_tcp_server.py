#import socket
import socket

#inisiasi socket TCP/IPv4
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind ke address dan port tertentu
tcp_sock.bind(('0.0.0.0', 6667))

#listen sebanyak 100
tcp_sock.listen(100)

while True:
    #terima req keneksi
    conn, client_address = tcp_sock.accept()
    
    #terima string dari client
    #parameter rcv besaran atau ukuran data yg dibaca
    #Stream block
    data = conn.recv(100)
    data = data.decode('utf-8')
    print(data)

    angka = int(data) % 2
    if angka == 0:
        #ubah data
        data = "OK - angka GENAP"
        #kirim ke client
        conn.send(data.encode('utf-8'))
    else:
        #ubah data
        data = "OK - angka GANJIL"
        #kirim ke client
        conn.send(data.encode('utf-8'))

    #tutup koneksi
    conn.close()
