N = int(input())

temp = N
for _ in range (temp):
    for i in range (1, N):
        print("*", end=" ")
    N -= 1
    print("*")