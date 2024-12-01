a_arr = input().split()
b_arr = input().split()
c_arr = input().split()

a_Eme = a_arr[0] == 'Y' and int(a_arr[1]) >= 37
b_Eme = b_arr[0] == 'Y' and int(b_arr[1]) >= 37
c_Eme = c_arr[0] == 'Y' and int(c_arr[1]) >= 37

#n_arr[0]이 Y이고 int(n_arr[1])이 >= 37 일때 A 이다.

# 첫번째 사람이 A인지 A가 아닌지로 케이스 2개로 나누어서 생각을 한다.

# 첫번째 a가 A일 때 b랑 c 둘 중 하나라도 위급상황 E로 처리
if a_Eme : # a가 A인 경우
    if b_Eme or c_Eme :
        print('E')
    else :
        print('N')
else :
    if b_Eme and c_Eme :
        print('E')
    else :
        print('N')

