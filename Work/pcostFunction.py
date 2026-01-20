
#this program is just modified pcost.py where we used function to run to open any file and 
#read its content and display the final cost
#currently its only portfolio.csv hardcoded here, instead of taking an input from user
#regarding which file to select for calculations!

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

cost = portfolio_cost('Data/missing.csv')
print('Total cost:' , cost)
        

