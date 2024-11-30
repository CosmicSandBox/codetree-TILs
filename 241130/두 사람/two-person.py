A = input().split()
B = input().split()

if (int(A[0]) >= 19 or int(B[0]) >= 19) and (int(A[1]) == M or int(A[0]) == M):
    print(1)
else :
    print(0)
