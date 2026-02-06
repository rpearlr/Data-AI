import matplotlib.pyplot as plt
import pandas as pd

attd = pd.read_csv("sales.csv")
df = pd.DataFrame(attd)
plt.barh(df['Product'],df['Price'])
plt.show()