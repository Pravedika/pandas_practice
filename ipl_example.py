import pandas as pd
df = pd.read_csv('IPL_Dataset.csv')
print(df)
print("Highest Runs:", df["Runs"].max())
print(df.head())
print("Highest Strike Rate:", df["Strike Rate"].max())
print(df.groupby('Team')['Average'].mean())
print(df.groupby('Team')['Average'].mean().rename('Average'))
print(df.groupby('Team')['Average'].mean().reset_index())