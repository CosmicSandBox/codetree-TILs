A, B = map(int, input().split())
sum_val = 0

for i in range (A, B+1, 1):
    if i % 5 == 0 :
        sum_val += i

print(sum_val)