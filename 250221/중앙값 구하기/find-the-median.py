A, B, C = map(int, input().split())

if A > B and A > C :
    if B>C :
        print(B)
    else :
        print(C)
else :
    if A > B or A > C :
        print(A)
    elif B > A and C > B:
        print(B)
    else :
        print(C)