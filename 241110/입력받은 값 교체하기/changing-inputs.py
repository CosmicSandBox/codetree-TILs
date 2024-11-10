"""
a, b = map(int, input().split())

temp = a
a = b
b = temp

print(a, b)
"""

inp = input()
arr = input().split()
a = int(arr[0])
b = int(arr[1])

temp = a
a = b
b = temp

print(a, b)