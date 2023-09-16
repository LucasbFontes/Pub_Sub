from google.cloud import pubsub_v1
from pymongo import MongoClient 
import json, os
from bson import json_util
import datetime

client = MongoClient('mongodb+srv://lucasbfontes17:r4vbh66bPnrl0qiM@mongodb-cluster.yioomlw.mongodb.net/')
collections  = r"/Users/lucasfontes/Documents/Estudo/The Plumbers/CC-GCP/device_2022_6_7_19_39_24.json"

with open (collections, 'r') as json_file:
    json_data = json.load(json_file)

service_account_key = r"/Users/lucasfontes/Documents/Estudo/The Plumbers/CC-GCP/local-2-bigquery-042cb468596b.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account_key

#print(json_data)

# TODO(developer)
project_id = "local-2-bigquery"
topic_id = "src_mongo_db"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

for data in json_data:
    #data_str = f"Message number {n}"
    # Data must be a bytestring

    timestamp_em_segundos = data["dt_current_timestamp"] / 1000

    # Criando um objeto datetime
    data_hora = datetime.datetime.fromtimestamp(timestamp_em_segundos)

    # Obtendo a data no formato ano-mês-dia
    data_formatada = data_hora.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    
    data["dt_current_timestamp"] = data_formatada
  
    json_file = (json.dumps(data).encode("utf-8"))
    # Add two attributes, origin and username, to the message
    future = publisher.publish(
       topic_path, json_file

    )
   # print(future.result())

print(f"Published messages with custom attributes to {topic_path}.")
