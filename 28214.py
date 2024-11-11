N,K,P = map(int, input().split())
li = list(map(int, input().split()))
pack = []

answer = 0

for i in range(1, N*K//K+1):
    pack.append(li[(i-1)*K:i*K])
    
for i in pack:
    if not i.count(0) >= P:
        answer += 1

print(answer)