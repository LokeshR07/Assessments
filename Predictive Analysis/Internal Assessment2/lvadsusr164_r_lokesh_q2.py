# -*- coding: utf-8 -*-
"""LVADSUSR164_R.LOKESH_Q2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rTj07t0-otBZhX0bzmBF_ubvdeH8JRsk
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import warnings
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
warnings.filterwarnings('ignore')

df = pd.read_csv('/content/Mall_Customers.csv')

df.info()

df.describe()

df.head()

df.isnull().sum()

df['Annual Income (k$)'] = df['Annual Income (k$)'].fillna(value=df['Annual Income (k$)'].mean())

df.isnull().sum()

df.duplicated().value_counts()

sns.boxplot(df)

for col in list(df.columns):
  sns.histplot(df[col])
  plt.show()

mapping = {'Male':1,'Female':0}
df['Gender'] = df['Gender'].map(mapping)
df['Gender'].value_counts()

edf = df.drop(columns = ['CustomerID'])

sns.heatmap(edf.corr(),annot=True)

# Scaler = MinMaxScaler()
# edf1 = Scaler.fit_transform(edf)

see = []
k_values = range(1, 10)
for k in k_values:
    kmeans = KMeans(n_clusters=k, init='k-means++', max_iter=300, n_init=10, random_state=42)
    kmeans.fit(edf)
    see.append(kmeans.inertia_)

plt.figure(figsize=(16, 6))
plt.plot(k_values, see, marker='o',color='#8B4513')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Within Cluster Sum of Squares')
plt.show()

kmeans = KMeans(n_clusters=3)
kmeans.fit(edf)
cluster_labels = kmeans.labels_
df['cluster'] =  kmeans.labels_

plt.figure(figsize=(15,10))
sns.scatterplot(data=df,x='Annual Income (k$)',y='Spending Score (1-100)',hue='cluster',palette='viridis', s=100)

silhouette_score(df,cluster_labels)

