input()
k = input()
hol = 0
zzac = 0

for j in k:
    i = int(j)
    if i == 0 or i % 2 == 0:
        zzac += 1
    else:
        hol += 1

if zzac > hol:
    print(0)
elif hol > zzac:
    print(1)
else:
    print(-1)
