prod = 1

a, b = map(int, input().split())

for i in range(b) :
    prod *= a

print(prod)