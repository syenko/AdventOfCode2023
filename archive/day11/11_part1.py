from itertools import combinations

f = open("input.txt", "r")
# f = open("test.txt", "r")

# helper function
def pretty_print(m):
    for row in m:
        print("".join(row))

# [row[col]
chars = [[char for char in x.strip()] for x in f]

NUM_COLS = len(chars[0])
NUM_ROWS = len(chars)

ans = 0

pretty_print(chars)

add_row = []
for i, line in enumerate(chars):
    if line.count(".") == NUM_COLS:
        add_row.append(i)

add_col = []
for col in range(NUM_COLS):
    line = [chars[i][col] for i in range(NUM_ROWS)]

    if line.count(".") == NUM_ROWS:
        add_col.append(col)

for row in add_row[::-1]:
    chars.insert(row, ["." for i in range(NUM_COLS)])

for col in add_col[::-1]:
    for row in chars:
        row.insert(col, ".")

print("************")
pretty_print(chars)

galaxies = []
INF = 1000000000
for row_num, row in enumerate(chars):
    for col_num, col in enumerate(row):
        if col == "#":
            galaxies.append((row_num, col_num))

pairs = list(combinations(galaxies, 2))

ans = 0
for first, second in pairs:
    ans += abs(second[0] - first[0]) + abs(second[1] - first[1])

print(ans)

f.close()