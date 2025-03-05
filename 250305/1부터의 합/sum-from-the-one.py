N = int(input())
sum_val = 0

for i in range (1, 101, 1):
    sum_val += i
    if sum_val >= N :
        break


print(i)