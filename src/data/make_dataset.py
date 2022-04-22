# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
import pandas as pd
from kafka import KafkaConsumer

from src.models.train_model import training_model


def check_user(pred):
    if pred == 0 or pred == 2:
        user = "Imposter"
    elif pred == 1:
        user = "genius"
    return user



def main():
    # """ Runs data processing scripts to turn raw data from (../raw) into
    #     cleaned data ready to be analyzed (saved in ../processed).
    # """
    # logger = logging.getLogger(__name__)
    # logger.info('making final data set from raw data')

    ## get the training data from the csv to df
    df = pd.read_csv("src\data\DSL-StrongPasswordData.csv")

   # training_model(df)

    ## run the kafka consumer
#     consumer = KafkaConsumer(
#         'ml-raw-dns',
#         bootstrap_servers=['localhost:9092'],
#         auto_offset_reset='earliest',
#         enable_auto_commit=False
#     )

#     # Ingesting data from input topic
#     for i, message in enumerate(consumer):
#         if i < 100:
#             msg = message.value.decode("utf-8")
#             pred = predict_model(msg)
#             prediction = check_user(pred)
#             print(prediction)
#         else:
#             break


if __name__ == '__main__':
#     log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
#     logging.basicConfig(level=logging.INFO, format=log_fmt)

#     # not used in this stub but often useful for finding various files
#     project_dir = Path(__file__).resolve().parents[2]

#     # find .env automagically by walking up directories until it's found, then
#     # load up the .env entries as environment variables
#     load_dotenv(find_dotenv())

    main()
