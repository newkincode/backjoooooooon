# 균형 잡히려면 len(s) = len(t) 여야한다
# 왼쪽에서만 s나 t를 하나 빼서 균형잡히게 만들어야함
N = int(input())
bad_stst__pronot__ = input()
yes_its_best_of_best_STST = 0

for i in range(N):
    if bad_stst__pronot__[i:].count("s") == bad_stst__pronot__[i:].count("t"):
        yes_its_best_of_best_STST = i
        break

print(bad_stst__pronot__[yes_its_best_of_best_STST:])