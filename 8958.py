for _ in range(int(input())):
    ox = input()

    count = 0
    count2 = 0


    for i in ox:
        if i == "O":
            count2 += 1
        else:
            count2 = 0
        count += count2
    print(count)