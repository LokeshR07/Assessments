# -*- coding: utf-8 -*-
"""LVADSUSR164_R.LOKESH_Q1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Y_Ud5z4yDfOg8ST3Gmf0z0EMJZSOXVHi
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_squared_error,accuracy_score,f1_score,precision_score,recall_score
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('/content/winequality-red.csv')

df.info()

df.shape

df.isnull().sum()

df.describe()

df.head()

for col in list(df.columns):
  df[col] = df[col].fillna(value = df[col].mean())

df.isnull().sum()

df.duplicated().value_counts()

df = df.drop_duplicates()

df.duplicated().value_counts()

plt.figure(figsize=(15,7))
sns.heatmap(df.corr(),annot=True)

plt.figure(figsize=(12,7))
sns.boxplot(df)

for col in list(df.columns):
  sns.histplot(df[col])
  plt.show()

q1 = df.quantile(0.25)
q3 = df.quantile(0.75)
IQR = q3 - q1
outliers = ((df < (q1 - 1.5*IQR)) | (df > (q3 + 1.5*IQR))).any(axis=1)
df = df[~outliers]
df.head()

df.info()

mapping = {3: 0, 4: 0, 5: 0, 6: 0, 7 : 1,8:1}
df['quality'] = df['quality'].map(mapping)
df['quality'].value_counts()

df.head()

X = df.drop(columns=['quality'])
Y = df['quality']

X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=52)

scaler=MinMaxScaler()
X_train=scaler.fit_transform(X_train)

X_test=scaler.transform(X_test)
model=RandomForestClassifier(n_estimators=80)
model.fit(X_train,y_train)

y_pred=model.predict(X_test)

print("Model score: ",model.score(X_test,y_test))
print("Percision score: ",precision_score(y_pred,y_test))
print("Recall score: ",recall_score(y_test,y_pred))

