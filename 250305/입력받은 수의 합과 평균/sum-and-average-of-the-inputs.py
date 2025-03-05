N = int(input())
sum_val = 0
cnt = 0

for i in range (N):
    a = int(input())
    sum_val += a
    cnt += 1

print(sum_val)
print(f"{sum_val/cnt:.1f}")


