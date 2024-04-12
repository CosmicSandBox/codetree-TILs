arr_lower_alp = [
    list(input().split())
    for _ in range(5)
]

for row in arr_lower_alp:
    for char in row:
        print(char.upper(), end=" ")
    print()