#import library flask
from flask import Flask, request

#inisiasi app flask sebagai server
app = Flask("Hello App")

#mendefinisikan fungsi yang akan handle method GET dengan URL '/'
@app.route('/', methods=['GET'])
def handle_get():
    return "Hello World!"

#jalankan server flask
app.run(port=7777)
