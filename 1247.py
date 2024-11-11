import sys
for i in range(3):
    n1 = int(sys.stdin.readline())

    s1 = 0

    for i in range(n1):
        s1+=int(sys.stdin.readline())
    
    if s1 == 0:
        print(0)
    elif s1 < 0:
        print("-")
    else:
        print("+")