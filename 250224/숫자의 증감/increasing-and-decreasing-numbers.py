C, N = input().split()
N = int(N)

a = 1

if C == 'A' :
    for k in range(N):
        print(a, end=" ")
        a += 1
elif C == 'D' :
    for i in range(N):
        print(N, end=" ")
        N -= 1