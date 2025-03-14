N = int(input())

temp = N
for _ in range (temp):
    for i in range (N):
        for j in range (N):
            print("*", end="")
        print(' ',end="")
    print()
    N -= 1
