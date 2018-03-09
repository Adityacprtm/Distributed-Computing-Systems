#import library http.client
import http.client
import json

ip_server = "127.0.0.1"
port_server = 7777

def get_mahasiswa():
    #kirim req GET dengan URL "/mahasiswa"
    #inisiasi koneksi ke server
    conn = http.client.HTTPConnection(ip_server, port=port_server)

    #kirim req ke server
    conn.request('GET', '/mahasiswa')

    #baca responese
    response = conn.getresponse().read()
    print( response.decode('utf-8') )

def tambah_mahasiswa():
    #kirim req GET dengan URL "/mahasiswa"
    #inisiasi koneksi ke server
    conn = http.client.HTTPConnection(ip_server, port=port_server)
    
    #definisi header
    header = {"Content-type" : "application/json"}

    #definisi body
    mahasiswa_baru = {'nim': 210, 'nama':'joni', 'Prodi':'SI'}

    #kirim req POST /mahasiswa
    conn.request('POST', '/mahasiswa', body=json.dumps(mahasiswa_baru), headers=header)

    #dapatkan response
    responese = conn.getresponse().read()
    print(responese.decode('utf-8'))

tambah_mahasiswa()
get_mahasiswa()
tambah_mahasiswa()
get_mahasiswa()