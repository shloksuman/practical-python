# pcost.py
import sys

def portfolio_cost(filename):
    f = open(filename , 'rt')
    header = next(f)
    # print(header)
    total_cost = 0

    for line in f:
        row = line.split(',')
        #print(row)
        try:
            total_cost+= int(row[1])*float(row[2])
        except ValueError:
            print('some dirty value, ignored')
        #print(row[1], row[2],int(row[1])*float(row[2]))
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
