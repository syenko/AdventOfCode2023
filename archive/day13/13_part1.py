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

ans = 0
count = 0
for num, group in enumerate(groups):
    rows = group[:]
    cols = ["".join([line[i] for line in group]) for i in range(len(group[0]))]

    failed = True
    # vertical
    for i in range(1, len(cols)):
        # print("center is {}".format(i))
        # print("max is {}".format(min(i, len(cols) - i)))
        failed = False
        for j in range(0, min(i-1, len(cols) - i - 1) + 1):
            # print("j is {}".format(j))
            # print(i - j - 1, i+j)
            # print(cols[i - j - 1])
            # print(cols[i + j])
            if cols[i-j-1] != cols[i+j]:
                failed = True
                break
        if not failed:
            ans += i
            print("vertical around {}".format(i))
            count += 1
            break

    if not failed:
        continue

    # horizontal
    for i in range(1, len(rows)):
        # print("center is {}".format(i))
        # print("max is {}".format(min(i, len(rows) - i) + 1))
        failed = False
        for j in range(0, min(i-1, len(rows) - i - 1) + 1):
            if rows[i - j - 1] != rows[i + j]:
                failed = True
                break
        if not failed:
            ans += 100*i
            print("horizontal around {}".format(i))
            count += 1
            break

    if failed:
        print("NO REFLECTION FOUND")
        print(num)

print(count, len(groups))
print(ans)

f.close()