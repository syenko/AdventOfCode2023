f = open("input.txt", "r")
# f = open("test.txt", "r")

lines = [x.strip() for x in f]

def pretty_print(m):
    for row in m:
        print("".join(row))

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
    "F": "SE",
    ".": "",
    "S": "NESW"
}

flip = {
    "N": "S",
    "S": "N",
    "E": "W",
    "W": "E"
}

start_row = 0
start_col = 0

# Get OG Pipe Chain
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

pipe_chain = [(2*curr_row, 2*curr_col)]

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
    pipe_chain.append((2*curr_row, 2*curr_col))

####### NEW STUFF

# double size of map
new_map = [["." for i in range(2 * NUM_COLS)] for j in range(2*NUM_ROWS)]
for row_num, row in enumerate(chars):
    for col_num, char in enumerate(row):
        new_map[row_num * 2][col_num * 2] = char

for row in range(0, 2*NUM_ROWS):
    for col in range(0, 2*NUM_COLS):
        if row % 2 == 1 or col % 2 == 1:
            if row - 1 >= 0 and row + 1 < 2 * NUM_ROWS \
                    and "S" in PIPES[new_map[row-1][col]] and "N" in PIPES[new_map[row+1][col]] \
                    and (row-1, col) in pipe_chain and (row + 1, col) in pipe_chain:
                new_map[row][col] = "|"
            elif col - 1 >= 0 and col + 1 < 2 * NUM_COLS \
                    and "E" in PIPES[new_map[row][col - 1]] and "W" in PIPES[new_map[row][col + 1]] \
                    and (row, col-1) in pipe_chain and (row, col + 1) in pipe_chain:
                new_map[row][col] = "-"
            else:
                new_map[row][col] = "."

pretty_print(new_map)

ans = 0

start_row = 0
start_col = 0

for row_num, row in enumerate(new_map):
    for col_num, char in enumerate(row):
        if char == "S":
            start_row = row_num
            start_col = col_num

curr_row = start_row
curr_col = start_col
last_dir = ""
# north
if start_row - 1 > 0 and new_map[start_row - 1][start_col] in "|F7":
    curr_row = start_row - 1
    last_dir = "N"
# south
elif start_row + 1 < NUM_ROWS and new_map[start_row + 1][start_col] in "|LJ":
    curr_row = start_row + 1
    last_dir = "S"
# west
elif start_col - 1 > 0 and new_map[start_row][start_col - 1] in "-J7":
    curr_col = start_col - 1
    last_dir = "W"
# east
elif start_col + 1 < NUM_COLS and new_map[start_row][start_col + 1] in "-LF":
    curr_col = start_col + 1
    last_dir = "E"

pipe_chain = [(curr_row, curr_col)]

count = 1
while curr_col != start_col or curr_row != start_row:
    count += 1
    # print(curr_row, curr_col)
    pipe = PIPES[new_map[curr_row][curr_col]]
    last_dir = flip[last_dir]

    # print(curr_row, curr_col)
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

pipe_map = [["X" if (row, col) in pipe_chain else "." for col in range(2*NUM_COLS)] for row in range(2*NUM_ROWS)]

visited = set()
next = []

for i in range(2*NUM_ROWS):
    if pipe_map[i][0] != "X":
        next.append((i, 0))
    if pipe_map[i][2*NUM_COLS - 1] != "X":
        next.append((i, 2*NUM_COLS - 1))

for i in range(2*NUM_COLS):
    if pipe_map[0][i] != "X":
        next.append((0, i))
    if pipe_map[2*NUM_ROWS - 1][i] != "X":
        next.append((2*NUM_ROWS - 1, i))

# floodfill
while len(next) != 0:
    row, col = next.pop(0)
    # print(row, col)
    if (row, col) in visited:
        continue
    print(row, col)
    visited.add((row, col))
    new_row = row + 1
    new_col = col + 1
    if row + 1 < 2*NUM_ROWS and pipe_map[row + 1][col] != "X" and (row + 1, col) not in visited:
        next.append((row + 1, col))
    if col + 1 < 2*NUM_COLS and pipe_map[row][col + 1] != "X" and (row, col + 1) not in visited:
        next.append((row, col + 1))
    if row - 1 > 0 and pipe_map[row - 1][col] != "X" and (row - 1, col) not in visited:
        next.append((row - 1, col))
    if col - 1 > 0 and pipe_map[row][col - 1] != "X" and (row, col - 1) not in visited:
        next.append((row, col - 1))

pretty_print(pipe_map)

for row, col in visited:
    pipe_map[row][col] = "*"

pretty_print(pipe_map)

count = 0
for row in range(0, 2*NUM_ROWS, 2):
    for col in range(0, 2*NUM_COLS, 2):
        if pipe_map[row][col] == ".":
            count += 1

print(count)

f.close()