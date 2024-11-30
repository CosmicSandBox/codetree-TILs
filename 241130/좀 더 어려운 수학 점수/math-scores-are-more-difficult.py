A_math, A_eng = map(int,input().split())
B_math, B_eng = map(int,input().split())

if A_math == B_math :
    if A_eng > b_eng :
        print('A')
    else :
        print('B')
else :
    higher_math = max(A_math, B_math)
    if higher_math == A_math:
        print('A')
    else :
        print('B')