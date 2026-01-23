test = { 'rahul' : 40, 'dinesh' : 22 , 'vikas' : 11 , 'raaaj' : 45 }

for name, age in test.items():
    print(f"Name: {name.capitalize()}, Age: {age:<9}")

# for name in test:
#     #print(name)
#     #print(test)
#     # print(test[name])
#     print('Name:' , name.capitalize() , ', Age:' , test[name])