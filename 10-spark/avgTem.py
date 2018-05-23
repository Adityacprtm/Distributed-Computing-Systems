from pyspark.sql import SparkSession, functions

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

df = spark.read.json("file:///data-kuliah/dataset/iot_devices.json")
# df.show()

# df.printSchema()

# df.select("cca3").show()

dfFilter = df.filter(df['cca3'] == "TCA")
dfSum = dfFilter.select(functions.sum(dfFilter.temp).alias('temp'))
#dfSum.show()

dfCount = df.groupBy("cca3").count()
dfFilterCount = dfCount.filter(dfCount['cca3'] == "USA").select('count')
dfFilterCount.show()

avg = dfSum['temp'] / dfFilterCount['count']
#avg.show()

#avg.saveAsTextFile("file:///data-kuliah/dataset/hasil_avg")
