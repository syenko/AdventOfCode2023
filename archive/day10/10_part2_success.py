# successful solution for part 2
f = open("input.txt", "r")
# f = open("test.txt", "r")

lines = [x.strip() for x in f]

# helper function
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

# given a map of chars, finds and returns a list of the pipe that forms the main loop
def get_pipe_chain(chars):
    num_rows = len(chars)
    num_cols = len(chars[0])
    start_row = 0
    start_col = 0

    # finds start row and column
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
    elif start_row + 1 < num_rows and chars[start_row + 1][start_col] in "|LJ":
        curr_row = start_row + 1
        last_dir = "S"
    # west
    elif start_col - 1 > 0 and chars[start_row][start_col - 1] in "-J7":
        curr_col = start_col - 1
        last_dir = "W"
    # east
    elif start_col + 1 < num_cols and chars[start_row][start_col + 1] in "-LF":
        curr_col = start_col + 1
        last_dir = "E"

    pipe_chain = [(curr_row, curr_col)]

    # iteratively go through the pipes
    while curr_col != start_col or curr_row != start_row:
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

    return pipe_chain

# Get OG Pipe Chain
doubled_pipe_chain = [(row * 2, col * 2) for row, col in get_pipe_chain(chars)]

# double size of map (so you can "squeeze through" pipes that are next to each other)
# basically, strategy is to add an extra row and column between every existing row / column so there are never two
# pipes next to each other
new_map = [["." for i in range(2 * NUM_COLS)] for j in range(2*NUM_ROWS)]
for row_num, row in enumerate(chars):
    for col_num, char in enumerate(row):
        new_map[row_num * 2][col_num * 2] = char

# this correctly fills in the added rows with pipes
# if a newly added space is between two pipes that were in the original pipe path, fill it with a connecting pipe
for row in range(0, 2*NUM_ROWS):
    for col in range(0, 2*NUM_COLS):
        # if one of the new spaces
        if row % 2 == 1 or col % 2 == 1:
            # checks the following
            # (1) is surrounded by two pipes
            # (2) pipes are in the right direction (vertical)
            # (3) pipes were in the original pipe chain
            if row - 1 >= 0 and row + 1 < 2 * NUM_ROWS \
                    and "S" in PIPES[new_map[row-1][col]] and "N" in PIPES[new_map[row+1][col]] \
                    and (row-1, col) in doubled_pipe_chain and (row + 1, col) in doubled_pipe_chain:
                new_map[row][col] = "|"
            # same for horizontal
            elif col - 1 >= 0 and col + 1 < 2 * NUM_COLS \
                    and "E" in PIPES[new_map[row][col - 1]] and "W" in PIPES[new_map[row][col + 1]] \
                    and (row, col-1) in doubled_pipe_chain and (row, col + 1) in doubled_pipe_chain:
                new_map[row][col] = "-"
            else:
                new_map[row][col] = "."

pretty_print(new_map)

pipe_chain = get_pipe_chain(new_map)

# creates a simplified pipe
pipe_map = [["X" if (row, col) in pipe_chain else "." for col in range(2*NUM_COLS)] for row in range(2*NUM_ROWS)]

visited = set()
next = []

# add all edges as places to check
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
    if (row, col) in visited:
        continue
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

# count number of unvisited (completely enclosed) spaces
count = 0
for row in range(0, 2*NUM_ROWS, 2):
    for col in range(0, 2*NUM_COLS, 2):
        if pipe_map[row][col] == ".":
            count += 1

print(count)

f.close()