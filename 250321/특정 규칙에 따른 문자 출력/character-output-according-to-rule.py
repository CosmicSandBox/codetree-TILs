"""
N = 2

공백 갯수 : 2, 0, / 2
문자 갯수 : 1, 2, / 1

  @
@ @
@

N = 3

공백 갯수 : 4, 2, 0 / 2, 4
문자 갯수 : 1, 2, 3 / 2, 1

    @
  @ @
@ @ @
@ @
@


"""

N = int(input())

for i in range (N): # 0, 1, 2
    for j in range (N-i):
        print(" ",end="")
    for k in range (i+1):
        print("@",end="")
    print()
for l in range (N-1): # 0, 1
    for m in range (N-2-(l+1)):
        print("@",end="")
    for n in range (l+1):
        print(" ",end="")
    print()
    
