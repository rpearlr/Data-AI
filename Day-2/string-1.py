full_name="Rhea Reddy"
words=full_name.split()
intial_1=words[0][0:1] + words[1][0:1]
print(intial_1)
intial_2 = "".join(word[0].upper() for word in full_name.split())
print(intial_2)