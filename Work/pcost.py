# pcost.py
#
# Exercise 1.27

f = open('Data/portfolio.csv' , 'rt')
header = next(f)
# print(header)
total_cost = 0

for line in f:
    row = line.split(',')
    #print(row)
    total_cost+= int(row[1])*float(row[2])
    print(row[1], row[2],int(row[1])*float(row[2]))

print('Total cost:',total_cost)
        