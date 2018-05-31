from pyspark import SparkContext

# Inisiasi spark context
sc = SparkContext.getOrCreate()

# Inisiasi rdd dari file text
rdd = sc.textFile("file:///data-kuliah/10-spark/ibubudi.txt")
#rdd = sc.textFile("file:///ibubudi.txt")

# Transform untuk split line
def split_line(line):
    return line.split(" ")
rddWord = rdd.flatMap(split_line)
x = rddWord.collect()
print(x)

# Beri angka 1 sebagai value
def give_number(word):
    return (word.lower(),1)
rddNumber = rddWord.map(give_number)
y = rddNumber.collect()
print(y)

# Hitung / jumlahkan value dengan key yang sama
def hitung(x,y):
    return x+y
hasil = rddNumber.reduceByKey(hitung)
z = hasil.collect()
print(z)

# Cetak output ke file
hasil.saveAsTextFile("file:///data-kuliah/10-spark/hasil_wordcount")
