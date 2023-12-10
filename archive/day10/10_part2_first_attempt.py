# my first try at part 2
# does not work for the case in which the enclosed area is inaccessible to the outside

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

pipe_chain = [(curr_row, curr_col)]

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
    pipe_chain.append((curr_row, curr_col))

pipe_map = [["X" if (row, col) in pipe_chain else "." for col in range(NUM_COLS)] for row in range(NUM_ROWS)]

visited = set()
next = []

for i in range(NUM_ROWS):
    if pipe_map[i][0] != "X":
        next.append((i, 0))
    if pipe_map[i][NUM_COLS - 1] != "X":
        next.append((i, NUM_COLS - 1))

for i in range(NUM_COLS):
    if pipe_map[0][i] != "X":
        next.append((0, i))
    if pipe_map[NUM_ROWS - 1][i] != "X":
        next.append((NUM_ROWS - 1, i))

while len(next) != 0:
    row, col = next.pop(0)
    # print(row, col)
    if (row, col) in visited:
        continue
    visited.add((row, col))
    new_row = row + 1
    new_col = col + 1
    if row + 1 < NUM_ROWS and pipe_map[row + 1][col] != "X" and (row + 1, col) not in visited:
        next.append((row + 1, col))
    if col + 1 < NUM_COLS and pipe_map[row][col + 1] != "X" and (row, col + 1) not in visited:
        next.append((row, col + 1))
    if row - 1 > 0 and pipe_map[row - 1][col] != "X" and (row - 1, col) not in visited:
        next.append((row - 1, col))
    if col - 1 > 0 and pipe_map[row][col - 1] != "X" and (row, col - 1) not in visited:
        next.append((row, col - 1))

for row in pipe_map:
    print("".join(row))

for row, col in visited:
    pipe_map[row][col] = "*"

for row in pipe_map:
    print("".join(row))

count = 0
for row in pipe_map:
    for char in row:
        if char == ".":
            count += 1

print(count)

f.close()