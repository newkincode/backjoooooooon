N = int(input())

X = list(map(int, input().split()))
L = list(map(int, input().split()))
C = list(input().split())

n = False

for i in range(N):
    for j in range(N):
        if abs(X[i] - X[j]) <= L[i] + L[j] and i != j and C[i] != C[j]:
            print(f"YES\n{i+1} {j+1}")
            n = True
            break
    if n == True:
        break

if n == False:
    print("NO")