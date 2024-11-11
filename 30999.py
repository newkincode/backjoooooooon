n, _ = input().split()
o_x = []

for i in range(int(n)):
    a = input()
    if a.count("O") > a.count("X"):
        o_x.append(True)
    elif a.count("O") < a.count("X"):
        o_x.append(False)

print(o_x.count(True))