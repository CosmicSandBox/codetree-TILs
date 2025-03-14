N = int(input())

a = 2

if N == 1 :
    print("*")
elif N >= 2 :
    for _ in range (N):
        for i in range(1, a-1, 1):
            print("*",end=" ")
        print("*")
        a += 1
    
