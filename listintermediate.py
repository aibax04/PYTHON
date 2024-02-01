# LIST

mylist = ["banana","cherry","apple"]
print (mylist)
print(type(mylist))

for i in mylist :
    print(i)
     
if "banana" in mylist:
    print("yes")

else :
    print ("no")

print(len(mylist))
mylist.append("lemon")
print(mylist)

mylist.insert(1 , "blueberry")
print(mylist)

item = mylist.pop()
print(item)
print(mylist)

item = mylist.remove("cherry") 
print (mylist)

mynumberlist = [2,3,4,5,6,372379,47,34957,49759,35]
item = mynumberlist.sort()
print(mynumberlist)

list2 = ["adhd","africa"]
newlist = list2 + mylist
print(newlist)

a = mynumberlist[:5]
print (a)

b = mynumberlist[::2]
print(b)

b = list2

print (list2)

a = [1,2,3,4,5]
b = [i*i for i in a]
print(b)


