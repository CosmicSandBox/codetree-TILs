sum = 0
cnt = 0

while True :
    n = int(input())
    if n >= 20 and n <= 29 :
        sum += n
        cnt += 1
    else :
        print(f"{sum/cnt:.2f}")
        break