N, M = map(int, input().split())

cardList = list(map(int, input().split()))

myMax = 0

for i in range(len(cardList)):
    for j in range(i+1, len(cardList)):
        for k in range(j+1, len(cardList)):
            if cardList[i]+cardList[j]+cardList[k] <= M:
                myMax = max(myMax, cardList[i]+cardList[j]+cardList[k])

print(myMax)