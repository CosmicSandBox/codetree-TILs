N = int(input())

for n in range (3, N+1, 3) :
    if (n % 3 == 0) or ((n - (n%10))%3 == 0) or ((n//10)%3 == 0) :
        print(0)
    else :
        print(n)