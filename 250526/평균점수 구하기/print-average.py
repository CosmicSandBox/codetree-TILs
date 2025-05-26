score_arr = input().split()
hap = 0 

for i in range (len(score_arr)):
    hap += float(score_arr[i])

print(f"{hap/8:.1f}")