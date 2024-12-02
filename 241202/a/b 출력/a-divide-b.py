a, b = map(int, input().split())

"""
answer_head = 0
answer_tail = 0
if a > b :
    answer_head = a//b
    for _ in range(21) :
        answer_tail += a%b*10 // b
    print(answer_head + answer_tail)

else :
    for i in range(1, 22) :
        temp_answer = 
        answer_tail += (a*10 // b) / 10**i
    print(answer_head + answer_tail)
"""

print(f"{a//b}.", end="")

a %= b

for _ in range (20) :
    print(a*10//b, end="")

    a = a*10%b