a, b = map(int,input().split())

while a <= b :
    if a % 2 != 0 :
        a *= 2
    elif a % 2 == 0 :
        a += 3
