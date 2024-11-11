
while True:
    inp = int(input())

    if inp == 0:
        break
    
    answer = 0

    for i in range(1,inp+1):
        answer += i*i

    print(answer)