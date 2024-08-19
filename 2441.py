num = int(input())
print("".join([f"{(num-i)*' '}{i*'*'}\n" for i in range(num, 0, -1)]))
