# 젓가락게임 시뮬레이션

YT, YJ = list(map(int, input().split()))
a = YT
b = YJ

while True:
    b += a
    if b >= 5:
        print("yt")
        break
    a += b
    if a >= 5:
        print("yj")
        break