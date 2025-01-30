"""
a, b, c = 5, 6, 7
temp_b = b
temp_c = c
b = a
c = temp_b
a = temp_c

print(f"{a}\n{b}\n{c}")
"""
a, b, c = 5, 6, 7
a, b, c = c, a, b

print(f"{a}\n{b}\n{c}")