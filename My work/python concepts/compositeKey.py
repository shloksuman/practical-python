#creating a composite key

hotels = {
    ('Delhi' , 101) : 'Rahul' ,
    ('Kanpur' , 101) : 'Akash'
}

#composite keys - multiple values used to create a SINGLE UNIQUE KEY

#accessing a value

print(hotels['Delhi' , 101])

#notice above , we didn't need to use any parentheses () to access the key tuples