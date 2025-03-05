N = int(input())
yak = 0

for i in range (1, N+1, 1):
    if N % i == 0 :
        yak += i

if yak == N :
    print('P')
else :
    print('N')
