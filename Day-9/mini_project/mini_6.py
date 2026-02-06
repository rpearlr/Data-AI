import pandas as pd 

data = {
    "t_id" : [1,2,3,4],
    "type" : ["deposit","withdraw","deposit","withdraw"],
    "amount" : [1000,300,1500,2000]
}

df=pd.DataFrame(data)
print(df)

deposit = df[df["type"]=="deposit"]
withdraw = df[df["type"]=="withdraw"]

print(deposit,"\n")
print(withdraw,"\n")

print("Balance : ",deposit['amount'].sum() - withdraw['amount'].sum(),"\n")

high_value = df[df["amount"] >= 1500 ]

print(high_value)