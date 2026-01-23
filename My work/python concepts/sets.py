names = ['IBM', 'AAPL', 'GOOG', 'IBM', 'GOOG', 'YHOO']

unique = set(names)
# unique = set(['IBM', 'AAPL','GOOG','YHOO'])

print(unique) #everytime this program run, hash values are calculated and items are stored randomly and
#hence they are printed different cuz they go to different places everytime program is run

#to print the items in sorted order , just use sorted method

print('Sorted Set:',sorted(unique))