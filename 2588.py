a = input()
b = int(input())

fst = 0
snd = 0
trd = 0

fst += int(a[-1]) * b

snd += int(a[-2]) * b

trd += int(a[-3]) * b

print(fst)
print(snd)
print(trd)
print(fst + snd + trd)