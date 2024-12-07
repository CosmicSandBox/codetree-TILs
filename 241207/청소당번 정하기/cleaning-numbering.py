# 2일마다 교실 청소
# 3일마다 복도 청소
# 12일마다 화장실 청소
# 날짜가 겹치면 주기가 더 긴 것읋 하기로

# n일 진행했을 때 각 장소의 청소 횟수를 차례로 출력

n = int(input())

cnt_classroom, cnt_hallway, cnt_restroom = 0, 0, 0

for i in range(1, n+1) :
    if i % 12 == 0 :
        cnt_restroom += 1
    elif i % 3 == 0 :
        cnt_hallway += 1
    elif i % 2 == 0 :
        cnt_classroom += 1

print(cnt_classroom, cnt_hallway, cnt_restroom)
