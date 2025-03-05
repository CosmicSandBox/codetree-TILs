import sys
input = sys.stdin.readline

prod = 1

A, B = map(int, input().split())

for i in range (1, B+1):
    if i % A == 0 :
        prod *= i
    
print(prod)