N = int(input())
temp = N
if N%2 != 0:
    temp_a = int(N-(N/2-1))
else :
    temp_a = int(N-(N/2))
for i in range (1,N+1,1): # 1, 2, 3, 4, 5
    if i % 2 != 0 :
        a=(i+1)//2
        for j in range(a):
            print("*",end=" ")
        print()
    else :
        for k in range(temp):
            print("*", end=" ")
        temp -= 1
        print()

for i in range (N,0,-1): # 1, 2, 3, 4, 5
    if i % 2 != 0 :
        a=(i+1)//2
        for j in range(a):
            print("*",end=" ")
        print()
    else :
        for k in range(temp_a+1):
            print("*", end=" ")
        temp_a += 1
        print()


    