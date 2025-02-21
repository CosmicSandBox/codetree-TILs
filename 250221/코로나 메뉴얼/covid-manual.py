import sys
input = sys.stdin.readline

A_symp, A_temp = input().split()
B_symp, B_temp = input().split()
C_symp, C_temp = input().split()

# Y + temp >= 37 -> A
# N + temp >= 37 -> B
# Y + temp < 37 -> C
# N + temp < 37 -> D

# A가 2명 이상이면 위급상황 -> E를 출력 그렇지 않으면 N을 출력

count = 0

if A_symp == 'Y' and int(A_temp) >= 37 :
    count += 1
if B_symp == 'Y' and int(B_temp) >= 37 :
    count += 1
if C_symp == 'Y' and int(C_temp) >= 37 :
    count += 1

if count >= 2 :
    print('E')
else :
    print('N')

