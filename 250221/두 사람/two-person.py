A_age, A_sex = input().split()
B_age, B_sex = input().split()

if (int(A_age) >= 19 and A_sex == "M") or (int(B_age) >= 19 and B_sex == "M") :
    print(1)
else :
    print(0) 