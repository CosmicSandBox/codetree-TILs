#공백 갯수 : 0, 2, 4, 6, 8 : 2*n
#별의 갯수 : 9, 7, 5, 3, 1 : 2*n-1

N = int(input())

"""for i in range (N):
    for j in range (2*i):
        print(" ",end="")"""

for k in range (N,0,-1):  # 5 4 3 2 1...
    for i in range (2*(N-k)): # 1 2 3 4 5
        print(" ",end="")
    for l in range (0, 2*k-1, 1):
        print("*",end=" ")
    print()

