# Import library xmlrpc server
import xmlrpc.server

# Inisiasi servernya
server = xmlrpc.server.SimpleXMLRPCServer( ("0.0.0.0", 7778) )

# Definisikan procedure/fungsi yang akan dipanggil dari client
def penjumlahan(a,b):
    c = a+b
    return "penjumlahan : " + str(c)

def pengurangan(a,b):
    c = a-b
    return "pengurangan : " + str(c)

def perkalian(a,b):
    c = a*b
    return "perkalian   : " + str(c)

def pembagian(a,b):
    c = a/b
    return "pembagian   : " + str(c)

def isPrima(a):
    if a > 2:
        for i in range(2,a):
            if (a % i) == 0:
                return str(a) + " bukan bilangan prima"
            else:
                return str(a) + " adalah bilangan prima"
    elif a == 2:
        return str(a) + " adalah bilangan prima"
    else:
        return "something wrong!"

# Daftarkan fungsi yang akan dipanggil dari client
server.register_function(penjumlahan, 'penjumlahan')
server.register_function(pengurangan, 'pengurangan')
server.register_function(perkalian, 'perkalian')
server.register_function(pembagian, 'pembagian')
server.register_function(isPrima, 'isPrima')
# Jalankan service servernya
server.serve_forever()
