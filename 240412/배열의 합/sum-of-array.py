n = 4

arr_2d = [
    list(map(int,input().split()))
    for _ in range(n)
]

sum = 0
for i in range (0, n, 1):
    for k in range (0, n, 1):
        sum += arr_2d[i][k]
    print(sum)
    sum = 0