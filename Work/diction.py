# prices = {} # Initial empty dict

# with open('Data/prices.csv', 'rt') as f:
#     for line in f:
#         row = line.split(',')
#         prices[row[0]] = float(row[1])

# above code was error one
#below is the fixed code

#solution 1

# prices = {}
# with open('Data/prices.csv', 'rt') as f:
#     for line in f:
#         row = line.split(',')
#         try:
#             prices[row[0]] = float(row[1])
#         except IndexError:
#             # If the line is empty, just ignore it and continue
#             continue
#         print(row[0] , row[1])

#solution 2

prices = {}
with open('Data/prices.csv', 'rt') as f:
    for line in f:
        row = line.split(',')
        # Only process if we have at least 2 items (Name and Price)
        if len(row) >= 2:
            prices[row[0]] = float(row[1])
            print(row[0] , row[1])