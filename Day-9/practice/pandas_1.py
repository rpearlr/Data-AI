import pandas as pd

data = {
    "Movie" : ["Dhurandar","Bazigar","Kubhi Khushi Kabhi Gam","Devdas"],
    "Genre" : ["Action","Drama","Comedy","Drama"],
    'Rating' : [5,3.5,4,5]
}

df=pd.DataFrame(data)
print(df)

print("Avg Rating : ",df["Rating"].mean(),"\n")

top_movies=df[df["Rating"] >= 4.5]
print(top_movies)
print()
low_movies = df[df["Rating"]<4]
print(low_movies)