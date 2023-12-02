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

    for round in rounds:
        cubes = round.split(", ")
        for cube in cubes:
            [count, color] = cube.split(" ")
            count = int(count)
            if color == "blue":
                if count > BLUE:
                    passed = False
                    break
            if color == "red":
                if count > RED:
                    passed = False
                    break
            if color == "green":
                if count > GREEN:
                    passed = False
                    break

        if not passed:
            break

    if passed:
        ans += id
        print("Passed!")


print(ans)

f.close()