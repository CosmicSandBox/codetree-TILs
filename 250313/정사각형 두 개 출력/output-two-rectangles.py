N = int(input())

for k in range (2):
    for i in range (N):
        for j in range (N-1): 
            print('*', end="")
        print('*')
    print(" ")