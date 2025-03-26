N = int(input())

# 첫 줄
print("* " * N)

# 위쪽: 1부터 N-1까지
for i in range(1, N):
    print("* " * i)

# 아래쪽: N-1부터 1까지
for i in range(N-1, 0, -1):
    print("* " * i)

# 마지막 줄
print("* " * N)