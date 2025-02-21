sex = int(input())
age = int(input())

if sex == 0 :
    if age >= 19 :
        print("MAN")
    elif age <= 19 :
        print("BOY")
else :
    if age >= 19 :
        print("WOMAN")
    elif age <= 19 :
        print("GIRL")