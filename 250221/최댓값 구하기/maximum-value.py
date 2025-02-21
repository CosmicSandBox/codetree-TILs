a, b, c = map(int, input().split())

if (a>=b and b>=c) or (a>=c and c>=b) :
    print(a)
elif (b>=a and a>=c) or (b>=c and c>=a):
    print(b)
else :
    print(c)