n = int(input())
sum_val = 0
cnt = 0

for i in range(n):
    a = int(input())
    sum_val += a
    cnt += 1

print(sum_val, end = " ")
print(f"{sum_val/cnt:.1f}")
