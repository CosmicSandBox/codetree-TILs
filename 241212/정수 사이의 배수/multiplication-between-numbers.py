a, b = map(int, input().split())
sum_val = 0
cnt = 0

for i in range(a, b+1) :
    if i % 7 == 0 or i % 5 == 0 :
        sum_val += i
        cnt += 1

print(sum_val, end = " ")
print(f"{sum_val/(b-a+1):.1f}")
        