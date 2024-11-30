a, b, c = map(int, input().split())

"""
minimum = 0

if a < b :
    minimum = a
else :
    minimum = b

if b < c :
    minimum = b
else :
    minimum = c

if c < a :
    minimum = c
else :
    minimum = a
"""

if a == min(a, b, c) : # 위에꺼 주석 해제하고 오른쪽 항에 minimum 넣어도 정답 처리됨
    print(1, end = " ")
else :
    print(0, end = " ")

if a == b and b == c :
    print(1, end = " ")
else :
    print(0, end = " ")