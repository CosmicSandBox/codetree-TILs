A, B = map(int, input().split())

s = A
while s <= B :
    print(s, end = " ")
    if s%2 != 0 :
        s *= 2
    else :
        s += 3
    