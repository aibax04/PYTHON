is_male = input("are you male : True  or False --> ")
is_tall = input("are you tall : true or false --> ")

if is_male and is_tall :
    print("you are a tall male ")
elif is_male and not(is_tall) :
    print("you are a short male")
elif not(is_male) and is_tall:
    print("you are not a male but are tall")
else:
    print("you are either not male or nor tall or both ")
