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

# 굳이 저렇게 if문 3개로 둘 필요없이
# if 2개만으로도 표현 가능한듯 -> 해설 보면 된다.
