a, b = map(int, input().split())
sum_val = 0

if a<b :
    for i in range(a, b+1, 1) :
        if i % 5 == 0:
            sum_val += i
    print(sum_val)

elif a>b :
    for i in range(b, a+1, 1) :
        if i % 5 == 0:
            sum_val += i
    print(sum_val)
else :
    if a % 5 == 0 :
        print(a)

