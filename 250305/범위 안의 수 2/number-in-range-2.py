sum_val = 0
cnt = 0

for i in range (10):
    a = int(input())
    if a >= 0 and a <= 200 :
        sum_val += a
        cnt += 1

print(sum_val, end =" ")
print(f"{sum_val/cnt:.1f}")