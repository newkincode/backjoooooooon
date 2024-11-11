# N*N 크기 안에 d,b,q,p 들이 들어 있음.
# D 안엔 1과 2가 들어있는데, 1은 상하 2는 좌우로 뒤집는다
# 뒤집은 결과 출력
"""
    d를 상하로 뒤집으면 q로, 좌우로 뒤집으면 b로 변한다.
    b를 상하로 뒤집으면 p로, 좌우로 뒤집으면 d로 변한다.
    q를 상하로 뒤집으면 d로, 좌우로 뒤집으면 p로 변한다.
    p를 상하로 뒤집으면 b로, 좌우로 뒤집으면 q로 변한다.
"""

N, D = map(int, input().split())

if D == 1:
    dbqpmap = {
        "d" : "q",
        "b": "p",
        "q": "d",
        "p": "b",
    }
elif D == 2:
    dbqpmap = {
        "d": "b",
        "b": "d",
        "q": "p",
        "p": "q",
    }

a = ""

for j in range(N):
    a = ""
    for i in input():
        a += dbqpmap[i]
    print(a)