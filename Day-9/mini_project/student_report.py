import matplotlib.pyplot as plt
import pandas as pd

student=pd.read_csv("student.csv")
df=pd.DataFrame(student)
print(df.isnull)
df['Age']=df['Age'].fillna(df['Age'].mean())
df['Marks']=df['Marks'].fillna(df['Marks'].mean())
df['City']=df['City'].str.strip().str.title()
print(df)
print("Average : ",df['Marks'].mean())
print("Top Scoring Student : \n",df.loc[df['Marks'].idxmax()])
print("Student below 70 : \n", df[df['Marks']<=70])

plt.bar(df['Name'],df['Marks'])
plt.show()