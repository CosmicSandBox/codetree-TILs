N = int(input()) # 5
temp = N
if N % 2 != 0 :
    a = int((N-1)//2)
else :
    a = int(N//2)

k = N-a
temp_a = a

for i in range (N): # 0, 1, 2, 3, 4
    if (N % 2 != 0 and i % 2 == 0) or (N%2 == 0 and i % 2 != 0):
        for j in range (temp):
            print("*",end=" ")
        temp -= 1
        print()

    else :
        for k in range (i):
            print("*",end=" ")
        print()

for l in range (N): # 0,1,2,3,4
    
    if (N % 2 != 0 and l % 2 == 0) or  (N%2 == 0 and l % 2 != 0):
        for m in range (k):
            print("*", end=" ")
        k += 1
        print()

    else :
        for n in range (temp_a):
            print("*", end=" ")
        temp_a -= 1
        print()
    
    



        

