list_a = list(map(int, input().split()))

sum = 0
average = 0
for i in range(0, len(list_a), 1):
    if list_a[i] >= 250:
        break
    sum += list_a[i]
    average = sum/i+1

print(sum, average)