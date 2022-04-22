import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tqdm import tqdm
import warnings

warnings.filterwarnings("ignore")
plt.style.use('ggplot')


def preprocessing_data(dataframe):
    """
          Args:
              df: A dataframe

          Returns:
              A preprocessing dataframe
          """

    dataframe['subject'] = dataframe['subject'].astype('category').cat.codes + 1
    subjects = dataframe["subject"]
    dataframe.drop(columns=['subject', 'sessionIndex', 'rep'], axis=1, inplace=True)

    return dataframe, subjects
