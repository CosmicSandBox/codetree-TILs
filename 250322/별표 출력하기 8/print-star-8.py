"""

N = 3
별 갯수 : 1 2 1

N = 4
별 갯수 : 1 2 1 4

N = 6
별 갯수 : 1 2 1 4 1 6



"""

N = int(input())

for i in range(1,N+1,1): # 1, 2, 3
    if i%2 != 0 :
        print("*")
    else :
        for j in range(i):
            print("*", end=" ")
        print()
