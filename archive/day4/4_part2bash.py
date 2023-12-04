f = open("input.txt", "r")
# f = open("test.txt", "r")

lines = [x.strip() for x in f]

ans = 0

new_cards = [i for i in range(len(lines))]

while len(new_cards) != 0:
    ans += 1
    card = new_cards.pop(0)

    line = lines[card]

    data = line.split(": ")[1]
    [winning, yours] = data.split(" | ")
    win_nums = [int(x.strip()) for x in winning.split()]
    your_nums = [int(x.strip()) for x in yours.split()]

    matched = 0
    for num in your_nums:
        if num in win_nums:
            matched += 1

    for j in range(matched):
        new_cards.append(j + card + 1)

print(ans)

f.close()