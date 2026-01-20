#JOIN , DELIMITER , basically prints list data with some characters in between like comman,
#dash, any symbol or anything

data = [ "hello" , "world" , "shlok"]
delim = " , "

result = delim.join([s.upper() for s in data])
print(result)  # hello , world , shlok is the output , since i made it upper case
# so output is HELLO, WORLD, SHLOK

for s in data:
    print(s.upper())