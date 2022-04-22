import json
import time
import pandas as pd
from kafka import KafkaProducer

df = pd.read_csv(r"E:\\uOttawa\\SecondTerm\\AI for CS\\elg7186-project-group_project_-7\\src\\data\\test_data.csv")
names = list(df.columns)


def json_serializer(data):
    return json.dumps(data).encode('utf-8')


producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=json_serializer
)

if __name__ == "__main__":
    for i, row in df.iterrows():
        message = dict(zip(names, row.values))
        print(message)
        producer.send('read-test', message)
        time.sleep(3)
