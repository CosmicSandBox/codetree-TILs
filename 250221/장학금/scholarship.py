import sys
input = sys.stdin.readline

mid, final = map(int,input().split())

if mid >= 90:
    if final >= 95 :
        print(100000, end=" ")
    elif final >= 90 :
        print(50000, end=" ")
    else :
        print(0)
else :
    print(0)