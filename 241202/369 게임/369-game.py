n = int(input())
# 1~n까지 369 게임을 진행한다 

# 3의 배수 or 3,6,9 중 하나라도 들어가 있으면 0을 출력 그렇지 않으면

for i in range (1, n+1):
    if i % 3 == 0 or (i % 10 in [3, 6, 9]) or (i - i%10 in [30, 60, 90]):
        print(0, end=" ")
    else:
        print(i, end=" ")