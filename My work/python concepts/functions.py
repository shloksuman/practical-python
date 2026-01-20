def sumcount(n):
    #returns sum of first n integers
    total=0
    while n>0:
        total+= n
        n -= 1
    return total

a = sumcount(5)
print(a)