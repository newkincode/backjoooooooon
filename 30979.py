t = input()
n = input()
f = list(map(int, input().split()))

f_sum = sum(f)

is_cry = "Padaeng_i Happy" if (int(t) - f_sum) <= 0 else "Padaeng_i Cry"

print(is_cry)