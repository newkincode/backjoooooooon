a = int(input())

answer = 0

for i in range(1, a+1):
    answer += (i*(i+1))+sum(range(i+1))

print(answer)