from pymongo import MongoClient
#from pydoop import hdfs
from sys import argv, exit
from bson.json_util import dumps
import json
import time
import datetime
import os

client = MongoClient('mongodb://192.168.56.121:27017/')
db = client.iot_db

if __name__ == "__main__":
    
    strg_ip = "127.0.0.1"
    strg_port = 7778


    while 1:
        try:

            print("Start Dump Data")
            logs = []
            for dta in db.sensor.find():
                logs.append(dta)
            #logs = db.sensor.find({'day':'morn'})
            #print(logs)
            
            '''
            key = ["morn","noon","night"]
            i = 0
            for i in range(0,2):
                keys = ['day']
                condition = {'day': key[i]}
                initial = {'count': 0, 'sum': 0}
                reduce = 'function(doc, out) { out.count++; out.sum += doc.temp; }'
                dt = db.sensor.group(key, condition, initial, reduce)
                print(dt)
            '''
            # Writing Data
            directory = "C:/Users/Aditya C. Pratama/Documents/GitHub/Sistem-Terdistribusi/sister/Analysis"
            #fileName = datetime.datetime.now().strftime("%d%m%y") + ".json"
            fileName = "iot_sensor.json"
            jsonData = json.dumps(json.loads(dumps(logs)))
            path = directory+"/"+fileName
            
            with open(path, "w") as h:
                h.write(jsonData)
                
            print("Success Dump Data")

            # Sleep
            time.sleep(300)

        except KeyboardInterrupt:
            print("BYE")
            exit()
