A = input().split()
B = input().split()

if (int(A[0]) >= 19 or int(B[0]) >= 19) and (A[1] == M or B[1] == M):
    print(1)
else :
    print(0)
