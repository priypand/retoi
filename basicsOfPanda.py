'''
    This program contains basics of pandas. It'll teach:-
    -> how to read a csv file using pandas
    -> rename columns
    -> replace missing values
    -> change data type of columns
'''

import pandas as pd
import numpy as np

path = "C:\myLearning\python\sample.csv"

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

# load the file and set headers equal to the value in the array
df = pd.read_csv(path, names=headers)

# print(df.head())                                                      # this line will print first 5 rows of dataframe

#####################################################################  OR  ######################################################################

# it'll stop python from naming headers
# df = pd.read_csv(path,header=None)
# df.columns = headers
# print(df.head())

## to replace missing values ? with NaN using numpy array; inplace = True will make changes in the dataframe
df.replace('?',np.nan,inplace=True);

## checking which values are null ; it'll create a new datafram missing_data with values true and false
missing_data = df.isnull()

### checking data types of columns:
print(df.dtypes)

### finding which columns have missing values:
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")


### finding data types of bore, stroke,horsepower, peak-rpm, price, normalized-losses
print(df[["bore","stroke","horsepower","peak-rpm","price","normalized-losses"]].dtypes)

### changing data types of bore, stroke,horsepower, peak-rpm, price, normalized-losses
df[["bore","stroke","horsepower","peak-rpm","price","normalized-losses"]] = df[["bore","stroke","horsepower","peak-rpm","price","normalized-losses"]].astype('float64')


### Replacing missing data with mean values
###     -> first find the mean value of the columns
###     -> then replace the value with the avg values


avg_bore = df['bore'].mean(axis=0)
df['bore'].replace(np.nan,avg_bore,inplace=True)

avg_stroke = df['stroke'].mean(axis=0)
df['stroke'].replace(np.nan,avg_stroke,inplace=True)

avg_horsepower = df['horsepower'].mean(axis=0)
df['horsepower'].replace(np.nan,avg_horsepower,inplace=True)

avg_peak = df['peak-rpm'].mean(axis=0)
df['peak-rpm'].replace(np.nan,avg_peak,inplace=True)

avg_price = df['price'].mean(axis=0)
df['price'].replace(np.nan,avg_price,inplace=True)

avg_normalized_losses = df['normalized-losses'].mean(axis=0)
df['normalized-losses'].replace(np.nan,avg_normalized_losses,inplace=True)

# will show which value is occurring the most
# print(df['num-of-doors'].value_counts().idxmax())
df['num-of-doors'].replace(np.nan,'four',inplace=True)
