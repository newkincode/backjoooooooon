n = int(input())

answer = 0

for i in range(n):
    answer += sum(map(int, input().split()))
print(answer)
