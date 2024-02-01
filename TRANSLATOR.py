#TRANSLATOR

def translate (phrase) :
    translation = ""
    for letter in phrase :
        if letter.lower() in "aeiou" :
            if letter.upper() in "AEIOU" :
               translation = translation + "g"
        else :
             translation=translation + letter
    return translation

print (translate(input("enter a phrase : ")))