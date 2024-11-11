size_map = {
    136: 1,
    142: 5,
    148: 10,
    154: 50,
}
print(sum([size_map[int(input().split()[0])] for _ in range(int(input()))]) * 1000)
