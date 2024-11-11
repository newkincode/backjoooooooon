n,w,h,l = map(int, input().split())

k = 0

world = [[0 for i in range(w)] for j in range(h)]

while True:
    try:
        for i in range(l):
            for j in range(l):
                world[i][j] = 1
    except:pass
    k += 1
