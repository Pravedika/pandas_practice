import pandas as pd
df = pd.read_csv('Ecommerce_Dataset.csv')
print(df)
print("Expensive Product:",df['Price'].max())
print("Cheapest Product: ",df['Price'].min())
print("Average Rating:",df['Rating'].mean())
print("Category wise product count:")
print(df.groupby('Category')['Product'].count())