mid, fin = map(int, input().split())

"""
# 이렇게 하면 풀리기는 하는데 모범 답안은 아닌듯
if mid >= 90:
    if fin >= 95 :
        print(100000)
    elif fin >= 90 :
        print(50000)
    else :
        print(0)
else :
    print(0)
"""

if mid >= 90 and fin >= 95 :
    print(100000)
elif mid >= 90 and fin >= 90 :
    print(50000)
else :
    print(0)