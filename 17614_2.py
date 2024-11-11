answer = 0
inp = input()

for i in range(1,len(inp)+1):
    answer += (int(inp)//(10**i))*3

print(answer)