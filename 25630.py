input()
st = input()

answer = 0

for i in range(len(st)//2):
    if st[i] != st[-(i+1)]:
        answer += 1
        
print(answer)