a, b, c = map(int, input().split())

# a가 중앙값이라고 가정하거나  중앙값이 아니라고 가정해서 (케이스 2개) 구해보자

if (a > b and a < c) or (a > c and a > c) :
    print(a)
else :
    if (b > c and a > b) or (c > b and b > a) :
        print(b)
    else :
        print(c)