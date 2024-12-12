# 완전수 : 자기 자신 제외한 약수 합이 자신이 되는 수

n = int(input())

sum_val = 0
result = 0

for i in range(n):
    if n%i == 0 :
        sum_val += i

if sum_val - n == n :
    print('P')
else :
    print('N')
    
        
