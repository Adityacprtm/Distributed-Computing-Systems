#import library flask
from flask import Flask, request
import json

#inisiasi app flask sebagai server
app = Flask("Hello App")

data_mahasiswa = [
    {
        "nim" : 123,
        "nama" : "Andi",
        "prodi" : "TIF"
    },
    {
        "nim" : 456,
        "nama" : "Budi",
        "prodi" : "TEKKOM"
    },
    {
        "nim" : 789,
        "nama" : "Sari",
        "prodi" : "SI"
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
    prodi = request.json['prodi']
    mahasiswa_baru = {
        'nama' : nama,
        'nim' : nim,
        'prodi' : prodi
    }
    #tambahkan ke list mahasiswa
    data_mahasiswa.append(mahasiswa_baru)
    return 'OK'

#fungsi update mahasiswa
@app.route('/mahasiswa/<nim>', methods=['PUT'])
def update_mahasiswa(nim):
    nim = [data_mahasiswa for data_mahasiswa in data_mahasiswa if data_mahasiswa['nim'] == nim]
    data_mahasiswa[0]['nama'] = request.json.get('nama', data_mahasiswa[0]['nama'])
    data_mahasiswa[0]['prodi'] = request.json.get('prodi', data_mahasiswa[0]['prodi'])
    return 'OK'

#fungsi delete mahasiswa
@app.route('/mahasiswa/<nim>', methods=['DELETE'])
def delete_mahasiswa(nim):
    nim = [data_mahasiswa for data_mahasiswa in data_mahasiswa if data_mahasiswa['nim'] == nim]
    data_mahasiswa.remove(data_mahasiswa[0])
    return 'OK - delete'


#jalankan server flask
app.run(port=7777)
