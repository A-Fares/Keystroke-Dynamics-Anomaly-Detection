from kafka import KafkaConsumer
from src.models.predict_model import predict_model
import json
import pandas as pd
import json
from pandas import json_normalize
from kafka import KafkaProducer


def forgiving_json_deserializer(v):
    try:
        return json.loads(v.decode('utf-8'))
    except json.decoder.JSONDecodeError:
        return None

def json_serializer(data):
    return json.dumps(data).encode('utf-8')
    
consumer = KafkaConsumer('read-test', bootstrap_servers='localhost:9092', auto_offset_reset='earliest',value_deserializer=forgiving_json_deserializer)
producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=json_serializer
    )
for i,message in enumerate(consumer):
    row=json_normalize(message.value)
    label,index=predict_model(row)
    row["label"]=label
    row["index"]=index
    names=list(row.columns)
    for i,row in row.iterrows():
        message = dict(zip(names, row.values))
        producer.send('input-events',message)
    