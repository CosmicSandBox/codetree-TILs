sum_val = 0
A, B = map(int, input().split())

for i in range (A, B+1, 1):
    sum_val += i

print(sum_val)
