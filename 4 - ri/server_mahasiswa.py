#import library flask, request dan jsonify
from flask import Flask, request, jsonify, abort

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
    data = [data for data in data_mahasiswa if data['nim'] == nim]
    #jika req yang tidak sesuai response 400 (bad req)
    if len(data) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'nim' in request.json and type(request.json['nim']) != int:
        abort(400)
    if 'nama' in request.json and type(request.json['nama']) is not str:
        abort(400)
    if 'prodi' in request.json and type(request.json['prodi']) is not str:
        abort(400)
    data[0]['nim'] = nim
    data[0]['nama'] = request.json.get('nama', data[0]['nama'])
    data[0]['prodi'] = request.json.get('prodi', data[0]['prodi'])
    return jsonify({'response':'Success Update'})

#fungsi delete mahasiswa method DELETE URL /mahasiswa/nim
@app.route('/mahasiswa/<int:nim>', methods=['DELETE'])
def delete_mahasiswa(nim):
    data = [data for data in data_mahasiswa if data['nim'] == nim]
    #jika req yang tidak sesuai response 400 (bad req)
    if len(data) == 0:
        abort(404)
    data_mahasiswa.remove(data[0])
    return jsonify({'response':'Success Delete'})

#fungsi yang akan handle method GET dengan URL '/mahasiswa'
@app.route('/mahasiswa', methods=['GET'])
#kembalikan data seluruh mahasiswa
def getAll_mahasiswa():
    return jsonify({'data_mahasiswa': data_mahasiswa})

@app.route('/mahasiswa/<int:nim>', methods=['GET'])
#kembalikan data mahasiswa tertentu method GET URL /mahasiswa/nim
def get_mahasiswa(nim):
    data = [data for data in data_mahasiswa if data['nim'] == nim]
    #jika url yg dimasukan tidak ditemukan di server, response 404
    if len(data) == 0:
        abort(404)
    return jsonify({'data_mahasiswa': data[0]})

#jalankan server flask
if __name__ == '__main__':
    app.run(port=7777)
    