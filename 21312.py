a,b,c = map(int, input().split())

# a b c
# a b
# a c
# b c
# a
# b
# c

kac = [a*b*c,a*b,a*c,b*c,b*c,a,b,c]
max_kac = 0

for i in kac:
    if i%2 != 0:
        max_kac = max(i, max_kac)

if max_kac == 0:
    for i in kac:
        max_kac = max(i, max_kac)

print(max_kac)