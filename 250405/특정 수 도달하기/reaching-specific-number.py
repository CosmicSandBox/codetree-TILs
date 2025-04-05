arr = list(map(int, input().split()))
arr2 = []
hap = 0

for i in arr:
    if i <= 250 :
        arr2.append(i)
    else :
        break

for j in arr2:
    hap += j

print(f"{hap} {hap/len(arr2):.1f}")