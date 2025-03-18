N = int(input())

for i in range (N):
    for j in range (N-i):
        print("*", end=" ")
    print()
for j in range (2, N+1, 1):
    for k in range (j):
        print("*", end=" ")
    print() 