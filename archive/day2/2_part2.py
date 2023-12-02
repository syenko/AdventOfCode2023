f = open("input.txt", "r")
# f = open("test.txt", "r")

lines = [x.strip() for x in f]

ans = 0

RED = 12
GREEN = 13
BLUE = 14

for line in lines:
    print(line)
    id = int(line.split(":")[0].split(" ")[1])
    rounds = line.split(": ")[1].split("; ")

    passed = True
    blue = []
    green = []
    red = []
    for round in rounds:
        cubes = round.split(", ")
        for cube in cubes:
            [count, color] = cube.split(" ")
            count = int(count)
            if color == "blue":
                blue.append(count)
            if color == "red":
                red.append(count)
            if color == "green":
                green.append(count)

    print(max(blue))
    print(max(green))
    print(max(red))

    ans += max(blue)*max(green)*max(red)


print(ans)

f.close()