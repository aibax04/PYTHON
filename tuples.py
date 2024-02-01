coordinates = [(4,5),(3,6),(1,9)] 
print(coordinates[0])

mytuple = (["max", 26, "boston"])
print(type(mytuple))

if input("enter a name : ") in mytuple :
    print("yes")
else :
    print("no")

print (len(mytuple))

mytuple.append("max")
print(mytuple)


print (mytuple.count("max"))

a = (1,2,3,4,5,6,7,8,9)
b = a [2:5]
print(b)

newtuple = ["simon", 28 ,"lucknow"]
name , age , city = newtuple
print (name)
print(age)
print(city)

tuple3 = (1,2,3,4,5,6)
b = [i*i for i in tuple3]
print (b)




