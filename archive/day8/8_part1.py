f = open("input.txt", "r")
# f = open("test.txt", "r")

lines = [x.strip() for x in f]

ans = 0

instructions = [char for char in lines[0]]

lines = lines[2:]
nodes = {line[0:3]:(line[7:10], line[12:15]) for line in lines}

curNode = "AAA"
count = 0
while curNode != "ZZZ":
    for instruction in instructions:
        if instruction == "L":
            curNode = nodes[curNode][0]
        else:
            curNode = nodes[curNode][1]
        count += 1
        if curNode == "ZZZ":
            break


print(count)

f.close()