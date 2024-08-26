N = int(input())

min_t = 1002

for i in range(N):
    a, b = map(int, input().split())
    
    if a <= b:
        min_t = min(min_t, b)
if min_t == 1002:
    print(-1)
else:
    print(min_t)