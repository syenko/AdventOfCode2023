f = open("input.txt", "r")
# f = open("test.txt", "r")

lines = [x.strip() for x in f]
instructions = lines[0].split(",")


def h_alg(char, start_val) -> int:
    start_val += ord(char)
    start_val *= 17
    start_val = start_val % 256
    return start_val


def h_on_str(str) -> int:
    start = 0
    for char in str:
        start = h_alg(char, start)

    return start


ans = 0
for instruction in instructions:
    ans += h_on_str(instruction)

print(ans)

f.close()
