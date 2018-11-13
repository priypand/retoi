import pandas as pd
import numpy as np

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

# load csv file
path = "C:\myLearning\python\sample.csv"
# set headers equal to the value in the array
df = pd.read_csv(path, names=headers)
# print first 5 rows
# print(df.head())
# will print the datatypes of all the columns
# print(df.dtypes)
# replace ? with NAN
df.replace("?", np.nan, inplace = True)
print(df.head())

# convert the data type of price from object to float
df[['price']] = df[['price']].astype('float64')

print(df.dtypes);
