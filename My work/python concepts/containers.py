# prices = []

# with open('"F:\Projects\practical-python\Work\Data\prices.csv"', 'rt') as f:
#     for line in f:
#         row = line.split(',')
#         prices[row[0]] = float(row[1])

prices = {} # Initial empty dict

# Insert new items
prices['GOOG'] = 513.25
prices['CAT'] = 87.22
prices['IBM'] = 93.37

keys = prices.keys()
print(keys)

items = prices.items()
print(items)

for k , v in items:
    print(k, "=" , v)