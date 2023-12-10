f = open("input.txt", "r")
# f = open("test.txt", "r")

lines = [x.strip() for x in f]

# chars[row][col]
chars = [[char for char in line] for line in lines]

NUM_ROWS = len(chars)
NUM_COLS = len(chars[0])

PIPES = {
    "|": "NS",
    "-": "EW",
    "L": "NE",
    "J": "NW",
    "7": "SW",
    "F": "SE"
}

flip = {
    "N": "S",
    "S": "N",
    "E": "W",
    "W": "E"
}

ans = 0

start_row = 0
start_col = 0

for row_num, row in enumerate(chars):
    for col_num, char in enumerate(row):
        if char == "S":
            start_row = row_num
            start_col = col_num

curr_row = start_row
curr_col = start_col
last_dir = ""
# north
if start_row - 1 > 0 and chars[start_row - 1][start_col] in "|F7":
    curr_row = start_row - 1
    last_dir = "N"
# south
elif start_row + 1 < NUM_ROWS and chars[start_row + 1][start_col] in "|LJ":
    curr_row = start_row + 1
    last_dir = "S"
# west
elif start_col - 1 > 0 and chars[start_row][start_col - 1] in "-J7":
    curr_col = start_col - 1
    last_dir = "W"
# east
elif start_col + 1 < NUM_COLS and chars[start_row][start_col + 1] in "-LF":
    curr_col = start_col + 1
    last_dir = "E"

count = 1
while curr_col != start_col or curr_row != start_row:
    count += 1
    # print(curr_row, curr_col)
    pipe = PIPES[chars[curr_row][curr_col]]
    last_dir = flip[last_dir]

    next_dir = pipe[int(not pipe.index(last_dir))]

    if next_dir == "S":
        curr_row += 1
    elif next_dir == "N":
        curr_row -= 1
    elif next_dir == "E":
        curr_col += 1
    elif next_dir == "W":
        curr_col -= 1

    last_dir = next_dir

print(count // 2)

f.close()