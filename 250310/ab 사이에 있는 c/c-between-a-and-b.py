a, b, c = map(int,input().split())

satisfied = True
for i in range (a, b+1):
    if i%c == 0 and i >= a and c <= b :
        satisfied = True
    else :
        satisfied = False

if satisfied == True :
    print("YES")
else :
    print("NO")
