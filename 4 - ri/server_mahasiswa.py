#import library flask
from flask import Flask, request
import json

#inisiasi app flask sebagai server
app = Flask("Hello App")

data_mahasiswa = [
    {
        "nim" : 123,
        "nama" : "Andi",
        "Prodi" : "TIF"
    },
    {
        "nim" : 456,
        "nama" : "Budi",
        "Prodi" : "TEKKOM"
    }
]

#mendefinisikan fungsi yang akan handle method GET dengan URL '/'
@app.route('/mahasiswa', methods=['GET'])
#kembalikan data seluruh mahasiswa
def handle_get():
    #konversi dari list/dictionary ke str format JSON
    return json.dumps(data_mahasiswa)

#fungsi handle tambah mahasiswa
@app.route('/mahasiswa', methods=['POST'])
def add_mahasiswa():
    #baca body req
    nim = request.json['nim']
    nama = request.json['nama']
    Prodi = request.json['Prodi']
    mahasiswa_baru = {
        'nama' : nama,
        'nim' : nim,
        'Prodi' : Prodi
    }
    #tambahkan ke list mahasiswa
    data_mahasiswa.append(mahasiswa_baru)
    return 'OK'

#jalankan server flask
app.run(port=7777)
