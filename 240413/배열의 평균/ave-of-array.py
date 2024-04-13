arr_2d = [
    list(map(int, input().split()))
    for i in range (2)
]

n = 0 # row length 값
m = 0 # column length 값

n = len(arr_2d)
m = len(arr_2d[0])

summ = 0
for i in range (n):
    summ = sum(arr_2d[i])/m
    print(round(summ, 1), end=' ')
    summ = 0
print()

for j in range (m):
    for k in range (n):
        summ += arr_2d[k][j]
        col_avg = summ/n
    print(round(col_avg, 1), end=" ")
    summ = 0
print()


for l in range (n):
    summ += sum(arr_2d[l])
all_avg = summ/(m*n)
print(round(all_avg, 1))