# 0을 제외해서 제일 길게 한 구간의 길이를 출력
n = int(input())
s = list(map(int, input().split()))

count = []
a = 0
for i in range(n):
    
    if s[i] != 0:
        a += 1
    else:
        
        count.append(a)
        a = 0
count.append(a)

print(max(count))