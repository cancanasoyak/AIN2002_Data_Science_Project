import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def nan_index(df):
    nan_index = []
    for i in range(len(df)):
        if df.iloc[i].isnull().any():
            nan_index.append(i)
    return nan_index



#real_data = pd.read_csv('Data/healthcare-dataset-stroke-data.csv')
#synthetic_data = pd.read_csv('Data/train.csv')


combined_data = pd.read_csv('Data/combined_data.csv')

print('age max' + str(combined_data['age'].max()) + '  /  age min' + str(combined_data['age'].min()))
print('avg_glucose_level max' + str(combined_data['avg_glucose_level'].max()) + '  /  avg_glucose_level min' + str(combined_data['avg_glucose_level'].min()))
print('bmi max' + str(combined_data['bmi'].max()) + '  /  bmi min' + str(combined_data['bmi'].min()))






""" sns.lineplot(combined_data,x = 'age',y = 'bmi')
plt.xlim(0, 5)
plt.show() """
