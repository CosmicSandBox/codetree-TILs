N = int(input())
temp_1 = 1
temp = N

if N%2 != 0 :
    temp_a = int(N+1//2)
    temp_b = int(N+1//2-1)
else :
    temp_a = int(N//2)
    temp_b = int(N//2-1)

for i in range (N,0, -1): # 5,4,3,2,1
    if i % 2 != 0 :
        for j in range(temp) :
            print("*", end=" ")
        temp-=1
        print()
    else :
        for k in range(temp_1):
            print("*", end=" ")
        temp_1 += 1
        print()

for i in range (1, N+1, 1): # 1,2,3,4,5
    if i % 2 != 0 :
        for j in range(temp_a-1):
            print("*", end=" ")
        temp_a += 1
        print()
    else :
        for k in range(temp_b-1):
            print("*", end=" ")
        temp_b -= 1
        print()

