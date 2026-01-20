arr = [ 1 , 3 , 6 , 'a']
total= 0
for k in arr:
    try:
        total+= k
    except TypeError:
        print('didn\'t add one value')

print('total is:', total)