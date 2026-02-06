import matplotlib.pyplot as plt
import pandas as pd
attd = pd.read_csv("attd.csv")
df = pd.DataFrame(attd)
plt.bar(df['Person'],df['Attendance'])
plt.show()