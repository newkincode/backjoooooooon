n, t, c, p = map(int, input().split())

# 여름: n
# 자라는데: t
# 칸수: c
# 가격: p
# n일 안에 t*c를 최대한 많이 분배해서 분배한 만큼을 p 에 곱하기
print(((n-1)//t)*c*p)