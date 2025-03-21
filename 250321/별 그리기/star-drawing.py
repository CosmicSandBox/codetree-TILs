"""
N = 2
별의 갯수 : 1, 3,/ 1
공백 갯수 : 1, 0,/ 1

N = 3
별의 갯수 : 1, 3, 5,/ 3, 1
공백 갯수 : 2, 1, 0,/ 1, 2

N = 4
별의 갯수 : 1, 3, 5, 7 / 5, 3, 1 (지금 4 2 0 이렇게 뜬다.)
공백 갯수 : 3, 2, 1, 0 / 1, 2, 3

N = 5
별의 갯수 : 1, 3, 5, 7, 9 / 7, 5, 3, 1
공백 갯수 : 4, 3, 2, 1, 0 / 1, 2, 3, 4

"""



N = int(input())

for i in range (N): # 0, 1, 2, 3
    for j in range(N-1-i):
        print(" ",end="")
    for k in range(1+2*i):
        print("*",end="")
    print()

for l in range (N-1): # 0, 1, 2
    for m in range (l+1):
        print(" ",end="")
    for n in range(2*N-3-2*l): # 5, 3, 1
        print("*",end="")
    print()
