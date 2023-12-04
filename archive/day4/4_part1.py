f = open("input.txt", "r")
# f = open("test.txt", "r")

lines = [x.strip() for x in f]

ans = 0

for line in lines:
    data = line.split(": ")[1]
    [winning, yours] = data.split(" | ")
    win_nums = [int(x.strip()) for x in winning.split()]
    your_nums = [int(x.strip()) for x in yours.split()]

    matched = 0
    for num in your_nums:
        if num in win_nums:
            matched += 1

    if matched > 0:
        ans += 2 ** (matched - 1)


print(ans)

f.close()