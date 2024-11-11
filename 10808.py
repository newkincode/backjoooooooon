text = input()

atoz=[chr(i) for i in range(97, 97+26)]

for i in atoz[:-1]:
    print(f"{text.count(i)} ", end="")
print(f"{text.count(atoz[-1])}")