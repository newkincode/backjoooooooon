input()

a = map(int, input().split())

answer = 0
answer1 = 0

for i in a:
    answer += i//30*10+10
    answer1 += i//60*15+15

if answer > answer1:
    print("M", answer1)
elif answer < answer1:
    print("Y", answer)
else:
    print("Y M", answer)