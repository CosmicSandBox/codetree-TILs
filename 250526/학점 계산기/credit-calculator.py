N = int(input())

score_arr = input().split()
hap = 0

for i in range (len(score_arr)):
    hap += float(score_arr[i])

avg = hap/N
print(f"{avg:.1f}");

if avg >= 4 :
    print('Perfect')
elif avg >= 3 :
    print('Good')
else :
    print('Poor')


