f = open("input.txt", "r")
# f = open("test.txt", "r")

lines = [x.strip() for x in f]

ans = 0

counts = [1 for i in range(len(lines))]

new_cards = [i for i in range(len(lines))]

for i in range(len(lines)):
    line = lines[i]

    data = line.split(": ")[1]
    [winning, yours] = data.split(" | ")
    win_nums = [int(x.strip()) for x in winning.split()]
    your_nums = [int(x.strip()) for x in yours.split()]

    matched = 0
    for num in your_nums:
        if num in win_nums:
            matched += 1

    for j in range(matched):
        counts[j + i + 1] += counts[i]

print(sum(counts))

f.close()