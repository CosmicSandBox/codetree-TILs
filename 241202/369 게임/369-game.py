n = int(input())
# 1~n까지 369 게임을 진행한다 

# 3의 배수 or 3,6,9 중 하나라도 들어가 있으면 0을 출력 그렇지 않으면

for i in range (1, n+1):

    if i % 3 == 0 or (i % 10 == 3 or 6 or 9) :
        print(0, end=" ")
    else:
        print(i, end=" ")