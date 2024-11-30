A_math, A_eng = map(int,input().split())
B_math, B_eng = map(int,input().split())

""" # 쓰레기 코드
if A_math == B_math :
    if A_eng > b_eng :
        print('A')
    else :
        print('B')
else :
    higher_math = max(A_math, B_math)
    if higher_math == A_math:
        print('A')
    else :
        print('B')
""" 

# 그냥 수학 점수가 더 높으면 그냥 높은애 출력 (차이가 나면)
# 수학 점수가 같다면 그땐 이제 영어를 비교

if A_math > B_math or (A_math == B_math and A_eng > B_eng ) :
    print('A')
else :
    print('B')