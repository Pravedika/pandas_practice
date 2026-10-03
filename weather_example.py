import pandas as pd
df = pd.read_csv('Weather_Dataset.csv')
print(df)
print("Average Temperature:",df['Temperature'].mean())
print("Hottest City:",df['Temperature'].max())
print("Coldest City:",df['Temperature'].min())
print("Cities above 35 degrees:")
print(df[df['Temperature']>35])
