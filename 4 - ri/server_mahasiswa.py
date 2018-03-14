#import library flask, request dan jsonify
from flask import Flask, request, jsonify, abort
import json

#inisiasi app flask sebagai server
app = Flask(__name__)

data_mahasiswa = [
    {
        "nim" : 123,
        "nama" : "Messi",
        "prodi" : "TIF"
    },
    {
        "nim" : 456,
        "nama" : "Iniesta",
        "prodi" : "TEKKOM"
    },
    {
        "nim" : 789,
        "nama" : "Pique",
        "prodi" : "SI"
    },
    {
        "nim": 111,
        "nama": "Andre",
        "prodi": "IPA"
    }
]

#fungsi index method GET URL /
@app.route('/', methods=['GET'])
def index():
    return "Hello, World!<br>I'm Aditya"

#fungsi menambah mahasiswa method POST URL /mahasiswa
@app.route('/mahasiswa', methods=['POST'])
def add_mahasiswa():
    #jika req yang tidak sesuai response 400 (bad req)
    if not request.json or not 'nim' in request.json:
        abort(400)
    #baca body req dan dimasukan ke var array/json
    mahasiswa_baru = {
        'nim': request.json['nim'],
        'nama': request.json['nama'],
        'prodi': request.json['prodi']
    }
    #tambahkan ke list data_mahasiswa
    data_mahasiswa.append(mahasiswa_baru)
    #mengembalikan value mahasiswa baru
    return jsonify({'data mahasiswa baru': mahasiswa_baru}), 201

#fungsi update mahasiswa method PUT URL /mahasiswa/nim
@app.route('/mahasiswa/<int:nim>', methods=['PUT'])
def update_mahasiswa(nim):
    #perulangan sebanyak index json data_mahasiswa
    for i in range(0, len(data_mahasiswa)):
        #pengecekan nim yang dicari dengan nim pd data_mahasiswa
        if nim == data_mahasiswa[i]['nim']:
            #update data mahasiswa
            data_mahasiswa[i]['nim'] = request.json['nim']
            data_mahasiswa[i]['nama'] = request.json['nama']
            data_mahasiswa[i]['prodi'] = request.json['prodi']
            return jsonify({'data_mahasiswa': data_mahasiswa})
    #jika nim tidak ditemukan
    abort(404)
    
#fungsi delete mahasiswa method DELETE URL /mahasiswa/nim
@app.route('/mahasiswa/<int:nim>', methods=['DELETE'])
def delete_mahasiswa(nim):
    #perulangan sebanyak index json data_mahasiswa
    for i in range(0, len(data_mahasiswa)):
        #pengecekan nim yang dicari dengan nim pd data_mahasiswa
        if nim == data_mahasiswa[i]['nim']:
            #hapus data_mahasiswa index ke i
            data_mahasiswa.remove(data_mahasiswa[i])
            return jsonify({'response': 'Success Delete'})
    #jika nim tidak ditemukan
    abort(404)

#fungsi yang akan handle method GET dengan URL '/mahasiswa'
@app.route('/mahasiswa', methods=['GET'])
#kembalikan data seluruh mahasiswa
def getAll_mahasiswa():
    return jsonify({'data_mahasiswa': data_mahasiswa})

@app.route('/mahasiswa/<int:nim>', methods=['GET'])
#kembalikan data mahasiswa tertentu method GET URL /mahasiswa/nim
def get_mahasiswa(nim):
    for i in range(0, len(data_mahasiswa)):
        if nim == data_mahasiswa[i]['nim']:
            return jsonify({'data_mahasiswa': data_mahasiswa[i]})
    #jika nim tidak ditemukan
    abort(404)

#jalankan server flask
if __name__ == '__main__':
    app.run(port=7777)
