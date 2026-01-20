print("Basically learning how string works in python, its syntaxes, methods")

a= "Data Science"

substr1 = a[0:]
substr2 = a[0:4]
substr3 = a[0:12]
substr4 = a[5:12]
substr5 = a[2:9]
substr6 = a[:10]
substr7 = a[-7:-3]
#the third parameter below is interesting , it jumps one step to pick the next character
#instead of normal 1 , which is default 1 , that means printing every character
substr8 = a[0::2]
#string reversal done by simple -1 in the third step parameter
substr9 = a[::-1]
substr10 = a[:]
substr11 = a[:].upper()
print(substr1)
print(substr2)
print(substr3)
print(substr4)
print(substr5)
print(substr6)
print(substr7)
print(substr8)
print(substr9)
print(substr10)
print(substr11)

#splitting a string, see the start stop parameters used!
split1 = a[:4]
split2 = a[4:]
print(split1)
print(split2)