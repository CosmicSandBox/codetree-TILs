n = int(input())
cnt_class = 0
cnt_aisle = 0
cnt_toilet = 0

# 2일마다 교실 청소
# 3일마다 복도 청소
# 12일 마다 화장실 청소

for i in range (n):
    if i % 2 == 0 and i % 3 != 0 and i % 12 != 0:
        cnt_class += 1
    elif i % 3 == 0 and i % 12 != 0 :
        cnt_aisle += 1
    elif i % 12 == 0 :
        cnt_toilet += 1

print(cnt_class, end=" ")
print(cnt_aisle, end=" ")
print(cnt_toilet, end=" ")