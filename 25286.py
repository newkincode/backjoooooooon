def is_onyear(year):
    if (year % 100 != 0 and year % 4 == 0) or year % 400 == 0:
        return True
    return False

onyear = [31,29,31,30,31,30,31,31,30,31,30,31]
justyear = [31,28,31,30,31,30,31,31,30,31,30,31]

for i in range(int(input())):
    y, m = map(int, input().split())
    
    if is_onyear(y):
        if m == 1:
            print(y-1, 12, onyear[m-2])
        else:
            print(y, range(1,12)[m-2], onyear[m-2])
    else:
        if m == 1:
            print(y-1, 12, justyear[m-2])
        else:
            print(y, range(1,12)[m-2], justyear[m-2])