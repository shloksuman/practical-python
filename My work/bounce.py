height = 100 #initial height of 100 metres
i = 1 # iterator
while i < 11 :
    print('i = ', i)
    print('height = ' , round(height, ndigits=4))
    height = 3*height/5
    i = i+1

name = input('please enter your name : ')
print('Program ran perfectly, Mr' , name)
