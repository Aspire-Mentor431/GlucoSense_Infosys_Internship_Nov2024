import pandas as pd
data = pd.read_csv("C:/Users/dell/OneDrive/Desktop/New folder/your_data.csv", delimiter=';')
print(data.head())
print(data.isnull().sum())
print(data.describe())
print(data['class'].value_counts())
