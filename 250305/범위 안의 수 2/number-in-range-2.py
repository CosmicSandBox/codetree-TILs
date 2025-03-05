sum_val = 0
cnt = 0

for i in range (10):
    a = int(input())
    if i >= 0 and i <= 200 :
        sum_val += i
        cnt += 1

print(sum_val)