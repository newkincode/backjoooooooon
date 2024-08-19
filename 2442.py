num = int(input())
print("".join([f"{(num-i)*' '}{(i*2-1)*'*'}\n" for i in range(1, num + 1)]))
