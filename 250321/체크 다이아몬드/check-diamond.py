"""

N = 3

공백 갯수 : 2, 1, 0, / 1, 2
별의 갯수 : 1, 2, 3, / 2, 1

  *
 * *
* * *
 * *
  *


N = 4

공백 갯수 : 3, 2, 1, 0, / 1, 2, 3
별의 갯수 : 1, 2, 3, 4, / 3, 2, 1

   *
  * *
 * * *
* * * *
 * * *
  * *
   *


"""



N = int(input()) # 4

for i in range (N): # 0, 1, 2, 3
    for j in range (N-1-i):
        print(" ",end="")
    for k in range (i+1):
        print("*",end=" ")
    print()
for l in range (N-1): # 0, 1, 2
    for m in range (l+1):
        print(" ",end="")
    for n in range (N-1-l):
        print("*",end=" ")
    print()