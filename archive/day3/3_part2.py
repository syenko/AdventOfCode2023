f = open("input.txt", "r")
# f = open("test.txt", "r")

# chars[row][column]
chars = [[c for c in x.strip()] for x in f]

ROWS = len(chars)
COLS = len(chars[0])


def useNum(row, colStart, colEnd):
    minRow = max(0, row - 1)
    maxRow = min(ROWS - 1, row + 1)
    minCol = max(0, colStart - 1)
    maxCol = min(COLS - 1, colEnd + 1)

    vals = [(chars[i][j], i, j) for i in range(minRow, maxRow + 1) for j in range(minCol, maxCol + 1)]
    # print(vals)

    for char, i, j in vals:
        if char == "*":
            return i, j

    return False


ans = 0
gears = {}

for row in range(ROWS):
    colStart = -1
    for col in range(COLS):
        # print(row, col)
        # print(chars[row][col].isnumeric())
        # start of phrase
        if colStart == -1 and chars[row][col].isnumeric():
            colStart = col
        # end of phrase
        if not chars[row][col].isnumeric() and not colStart == -1:
            vals = useNum(row, colStart, col - 1)
            num = int("".join(chars[row][colStart:col]))
            if vals:
                if vals in gears.keys():
                    gears[vals].append(num)
                else:
                    gears[vals] = [num]
            colStart = -1

    if colStart != -1:
        vals = useNum(row, colStart, COLS - 1)
        num = int("".join(chars[row][colStart:COLS]))
        if vals:
            if vals in gears.keys():
                gears[vals].append(num)
            else:
                gears[vals] = [num]

for key, val in gears.items():
    print(key, val)
    if len(val) == 2:
        ans += val[0] * val[1]

print(ans)

f.close()
