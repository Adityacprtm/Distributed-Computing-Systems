import sys
from pyspark import SparkContext, SparkConf

key = str(sys.argv[1])
spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

def normalize(sc, data):
    rdd1 = data.map(lambda x: (x.split(" ")[0], float(x.split(" ")[1])))
    rdd2 = data.map(lambda x: (x.split(" ")[2], float(x.split(" ")[3])))
    rdd3 = data.map(lambda x: (x.split(" ")[4], float(x.split(" ")[5])))
    rdd4 = data.map(lambda x: (x.split(" ")[6], float(x.split(" ")[7])))
    rdd = sc.union([rdd1, rdd2, rdd3, rdd4])
    return rdd


def average(data):
    sumCount = data.combineByKey(lambda value: (value, 1),
                                 lambda x, value: (x[0] + value, x[1] + 1),
                                 lambda x, y: (x[0] + y[0], x[1] + y[1]))

    averageByKey = sumCount.map(lambda (label, (value_sum, count)): (label, value_sum / count))
    return averageByKey.collect()


def main():
    key = str(sys.argv[1])
    #conf = SparkConf().setAppName("Average all data").setMaster("spark://node1:7077")
    sc = SparkContext.getOrCreate()
    rdd = spark.read.json("file:///data-kuliah/sister/Analysis/300518/1255.json")
    normal = normalize(sc, rdd)
    print(normal)
    # find average
    output = average(normal)
    print(output)
    file = open("/home/vagrant/avg" + key, "w")
    for(key, value) in output:
        file.write(key + ': ' + str(value) + "\r\n")
    file.close()
    sc.stop()


if __name__ == "__main__":
    main()
