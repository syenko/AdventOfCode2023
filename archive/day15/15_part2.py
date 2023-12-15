f = open("input.txt", "r")
# f = open("test.txt", "r")

lines = [x.strip() for x in f]
instructions = lines[0].split(",")

ans = 0

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

boxes = [{} for i in range(256)]

for instruction in instructions:
    if "=" in instruction:
        key, length = instruction.split("=")
        length = int(length)
        box = h_on_str(key)

        boxes[box][key] = length

    elif "-" in instruction:
        key = instruction[:-1:]
        box = h_on_str(key)
        if key in boxes[box].keys():
            del boxes[box][key]

    # ans += h_on_str(instruction)

for i, box in enumerate(boxes):
    if len(box.keys()) > 0:
        print("box {}: {}".format(i, box))

        for lens_num, lens in enumerate(box.values()):
            ans += (1 + i) * (lens_num + 1) * lens

print(ans)

f.close()