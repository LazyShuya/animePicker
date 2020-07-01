import pandas as pd
from pandasql import sqldf

df =pd.read_csv('test.csv')
print(df.anime.unique()[0])