cnt_3 = 0
cnt_5 = 0

for i in range(10):
    a = int(input())
    if a % 3 == 0 and a % 5 == 0 :
        cnt_3 += 1
        cnt_5 += 1
    elif a % 3 == 0 :
        cnt_3 += 1
    elif a % 5 == 0 :
        cnt_5 += 1

print(f"{cnt_3} {cnt_5}")
