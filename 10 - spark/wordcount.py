from pyspark import SparkContext

#inisiasi spark context

sc = SparkContext.getOrCreate()

# inisiasi rdd dari file text
rdd = sc.textFile("file:///vagrant/ibubudi.txt")

# transform untuk split line
def split_line(line):
    return line.split(" ").lower()
rddWord = rdd.flatMap(split_line)

# beri angka 1 sebagai value (key,value)
def give_number(word):
    return (word,1)
rddNumber = rdd.map(give_number)

# jumlahkan value dengan key yg sama
def hitung(x,y):
    return x+y
hasil = rddNumber.reduceByKey(hitung)

hasil.saveAsTextFile("file:///vagrant/hasil_wordcount")

# vagrant share folder dimana lokasi vagrantfile
