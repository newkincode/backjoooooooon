import sys

scores = []

for i in range(int(sys.stdin.readline())):
    inp = list(map(int, sys.stdin.readline().split()))
    run_1st = inp[0]
    run_2nd = inp[1]
    trick = inp[2:]
    
    scores.append(max(trick))
    trick.remove(scores[i])
    scores[i] += max(trick)
    scores[i] += max(run_1st, run_2nd)

print(max(scores))