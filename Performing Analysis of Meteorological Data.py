#!/usr/bin/env python
# coding: utf-8


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r"C:\Users\Anshu Shah\Downloads\weatherHistory.csv")


print(df)


pd.read_csv(r"C:\Users\Anshu Shah\Downloads\weatherHistory.csv")


titles_req = ["Formatted Date", "Apparent Temperature (C)", "Humidity"]
df = df[titles_req]


df['Formatted Date'] = pd.to_datetime(df['Formatted Date'], utc=True)
df = df.set_index('Formatted Date')
df = df.resample('MS').mean()


df.head()


plt.figure(figsize=(14,6))
plt.title("Variation in Apparent Tempearture and Humidity with time")
plt.plot(df)


df_april = df[df.index.month==4]


plt.figure(figsize=(14,6))
plt.plot(df_april)




