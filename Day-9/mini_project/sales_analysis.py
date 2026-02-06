import pandas as pd

df = pd.read_csv("sales.csv")
total_sales = df.copy()
df['total'] = df['Price'] * df['Quantity']
print(df,"\n")

best_product = df.loc[df['total'].idxmax()]
print("Best Sales :\n",best_product,"\n")
df["Prie with Tax"] = df["Price"] * 1.1
print(df)