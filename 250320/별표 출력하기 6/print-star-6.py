"""
N == 2

* * *
  *
* * *

공백 갯수 : 0, 2, / 0
별의 갯수 : 3, 1, / 3

-----------------------------------

N == 3

* * * * *
  * * *
    *
  * * *
* * * * *

공백 갯수 : 0, 2, 4, / 2, 0
별의 갯수 : 5, 3, 1, / 3, 5


N == 4

공백 갯수 : 0, 2, 4, 6, / 4, 2, 0    // descend는 0+(N-2)*2 부터 시작해서 -2씩 줄어듦
별의 갯수 : 7, 5, 3, 1, / 3, 5, 7   -> 1+(N-1)*2 부터 시작해서 -2씩 줄어듦 // ascend는 3부터 시작해서 2씩 늘어난다

"""



N = int(input())

for i in range(N): #0,1,2,4
    for j in range(i*2):
        print(" ",end="")
    for k in range((1+(N-1)*2)-2*i):
        print("*",end=" ")
    print()

for l in range(N-1): #0,1,2
    for m in range((N-2)*2-2*l):
        print(" ",end="")
    for n in range(3+2*l):
        print("*",end=" ")
    print()
    


