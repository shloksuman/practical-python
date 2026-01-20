with open('Data/portfolio.csv' , 'rt') as f:
        data = f.read() #read everything all at once as a string

data
#print(data)

# with open('Data/portfolio.csv', 'rt') as f2:
#     for line in f2:
#         print(line, end='') # end='' prevents double spacing


#reading only first line
'''
this is a comment 
multi line comments
used triple quotes
you can use double quotes as well
'''

f3 = open('Data/portfolio.csv' , 'rt') 
headers = next(f3)
headers1 = next(f3)
headers2 = next(f3)

print(headers)
print(headers1)
print(headers2)

for line in f3:
        row = line.split(',')
        print(row)

f3.close()