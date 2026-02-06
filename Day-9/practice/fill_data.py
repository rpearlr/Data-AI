import pandas as pd
sale = pd.read_csv("sales.csv")
df = pd.DataFrame(sale)
print(df.isnull())
df.fillna({'Price':df['Price'].mean()},inplace=True)
df['Quantity']  = df['Quantity'].fillna(df['Quantity'].mean())
print(df,"\n")
# print(d)