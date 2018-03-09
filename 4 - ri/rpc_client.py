#Import xmlrpc client
import xmlrpc.client

# Koneksikan ke server RPC
proxy = xmlrpc.client.ServerProxy("http://127.0.0.1:7778/")

# Panggil fungsinya
hasil_penjumlahan = proxy.penjumlahan(50, 10)
print(hasil_penjumlahan)
hasil_pengurangan = proxy.pengurangan(50, 10)
print(hasil_pengurangan)
hasil_perkalian = proxy.perkalian(50, 10)
print(hasil_perkalian)
hasil_pembagian = proxy.pembagian(50, 10)
print(hasil_pembagian)
hasil_prima = proxy.isPrima(2)
print(hasil_prima)
