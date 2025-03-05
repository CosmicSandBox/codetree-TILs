import sys
input = sys.stdin.readline

cnt = 0

N = int(input())

for i in range (1, N+1, 1):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 :
        cnt += 1

print(N-cnt)