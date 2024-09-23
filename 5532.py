import math
L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

# 방학 L
# 수학 B
# 국어 A
# 하루국어 C
# 하루수학 D

DB = math.ceil(B / D)
DA = math.ceil(A / C)
nol = L - max(DA, DB)

print(nol)