"""
N = 2
별의 갯수 : 1, 3,/ 1
공백 갯수 : 1, 0,/ 1

N = 3
별의 갯수 : 1, 3, 5,/ 3, 1
공백 갯수 : 2, 1, 0,/ 1, 2

"""



N = int(input())

for i in range (N): # 0, 1, 2
    for j in range(N-1-i):
        print(" ",end="")
    for k in range(1+2*i):
        print("*",end="")
    print()

for l in range (N-1): # 0, 1
    for m in range (l+1):
        print(" ",end="")
    for n in range(N-2*l):
        print("*",end="")
    print()