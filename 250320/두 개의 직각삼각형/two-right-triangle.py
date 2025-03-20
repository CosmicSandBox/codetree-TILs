"""
N == 4

********
***  ***
**    **
*      *

별 4 공백 0 별 4
별 3 공백 2 별 3
별 2 공백 4 별 2
별 1 공백 6 별 1

총 합은 8이다

두번째 부턴 : 별 N / 공백 2(등비2) / 별 N(등차-1)


******
**  **
*    *

별 3 공백 0 별 3
별 2 공백 2 별 2
별 1 공백 4 별 1

"""

N = int(input())

for i in range (N,0,-1):  # 4 3 2 1
    for j in range (i): 
        print("*", end="")

    for k in range ((N-i)*2): 
        print(" ",end="")

    for l in range (i):
        print("*", end="") 
    print()
