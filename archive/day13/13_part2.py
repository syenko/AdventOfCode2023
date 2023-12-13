f = open("input.txt", "r")
# f = open("test.txt", "r")

lines = [x.strip() for x in f]

groups = []
cur_group = []
for line in lines:
    if line == "":
        groups.append(cur_group)
        cur_group = []
        continue

    cur_group.append(line)
groups.append(cur_group)

def findLine(lines) -> int:
    # vertical
    for i in range(1, len(lines)):
        # print("center is {}".format(i))
        # print("max is {}".format(min(i, len(cols) - i)))
        mistakes = 0
        for j in range(0, min(i - 1, len(lines) - i - 1) + 1):
            # print("j is {}".format(j))
            # print(i - j - 1, i+j)
            # print(lines[i - j - 1])
            # print(lines[i + j])
            left_line = lines[i - j - 1]
            right_line = lines[i + j]
            count_mis = sum([1 if left_line[i] != right_line[i] else 0 for i in range(len(left_line))])
            mistakes += count_mis

            # print("num_mistakes = {}".format(count_mis))

            if mistakes >= 2:
                break

        if mistakes == 1:
            return i

    return -1

ans = 0
count = 0
for num, group in enumerate(groups):
    rows = group[:]
    cols = ["".join([line[i] for line in group]) for i in range(len(group[0]))]

    vert = findLine(cols)
    if vert != -1:
        ans += vert
        print("vertical around {}".format(vert))
        count += 1
        continue

    hor = findLine(rows)
    if hor != -1:
        ans += 100 * hor
        print("horizontal around {}".format(hor))
        count += 1
        continue

    print("NO REFLECTION FOUND")
    print(num)

print(count, len(groups))
print(ans)

f.close()