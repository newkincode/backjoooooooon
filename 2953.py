il = sum(map(int, input().split()))
e= sum(map(int, input().split()))
sam= sum(map(int, input().split()))
sa= sum(map(int, input().split()))
o= sum(map(int, input().split()))

li = [il,e,sam,sa,o]

print(li.index(max(li))+1, max(li))

