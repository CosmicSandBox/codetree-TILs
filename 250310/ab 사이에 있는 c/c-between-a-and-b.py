a, b, c = map(int,input().split())

satisfied = 0
for i in range (a, b+1):
    if i%c == 0 and i >= a and c <= b :
        satisfied += 1
    else :
        continue

if satisfied >= 1 :
    print("YES")
else :
    print("NO")
