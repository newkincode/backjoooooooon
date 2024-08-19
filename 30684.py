a = []

for _ in range(int(input())):
    a.append(input())
b = []
for i in a:
    if len(i) == 3:
        b.append(i)
print(sorted(b)[0])