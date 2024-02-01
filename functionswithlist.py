lucky_number = [4,10,29,3,25]
friends = ["kevin","karen","jim","oscar"]
friends.extend(lucky_number)
friends.append("creed")              # to add something into the list
friends.insert(0,"kelly")            # to add something at an index number
friends.remove("jim")                # to remove something from the list
#friends.clear()                     # to clear the complete list
friends.pop()
#friends.sort()                      #arrange the list in ascending order
print(friends)
print(friends.index("oscar"))        # to check the index of a member in a list

lucky_number.sort()
print(lucky_number)
lucky_number.reverse()               #reverse the order of a string
print(lucky_number)

friends2 = friends.copy              #copy one string in other
