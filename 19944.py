n,m = input().split()

if int(m) == 1 or int(m) == 2:
    print("NEWBIE!")
elif int(m) <= int(n) and not (int(m) == 1 or int(m) == 2):
    print("OLDBIE!")
else:
    print("TLE!")
