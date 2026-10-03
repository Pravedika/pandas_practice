import pandas as pd
df = pd.read_csv('Bank_Dataset.csv')
print(df)
print("Highest Balance :", df['Balance'].max())
print("Lowest Balance:", df['Balance'].min())
print("Customers with loan >5lakh are:") 
print(df[df['Loan']>500000])
print("Total Balance: ",df['Balance'].sum())
print(df.groupby('City')['Name'].count())
