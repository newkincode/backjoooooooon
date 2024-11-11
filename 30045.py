textlist = []
answer = 0

for i in range(int(input())):
    inp = input()
    if inp.count("01") > 0 or inp.count("OI") > 0:
        answer += 1
        continue
    
print(answer)