add = lambda a,b : a+b
print(add(8,2))
num = [1,2,3,4,5,6,7,8]
even = list(filter(lambda x:x%2==0,num))
print(even)
data=[
  {'name' : 'Alice' , 'age' : 21},
  {'name': 'Bob' ,  'age' : 22},
  { 'name' : 'Charlie' , 'age':34}
]

young = min(data,key=lambda x:x['age']<30)
print(young)