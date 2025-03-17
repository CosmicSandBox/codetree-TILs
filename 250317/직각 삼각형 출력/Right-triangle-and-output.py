N = int(input())

if N == 1:
    print("*")
else :
    for i in range (N):
        print("*", end="")
        print("**"*i)
        
