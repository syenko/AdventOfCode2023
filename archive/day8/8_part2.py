import math

f = open("input.txt", "r")
# f = open("test.txt", "r")

lines = [x.strip() for x in f]

ans = 0

instructions = [char for char in lines[0]]

lines = lines[2:]
nodes = {line[0:3]:(line[7:10], line[12:15]) for line in lines}

counts = {}

for node in nodes.keys():
    if node[2] == "A":
        curNode = node
        count = 0
        while curNode[2] != "Z":
            for instruction in instructions:
                if instruction == "L":
                    curNode = nodes[curNode][0]
                else:
                    curNode = nodes[curNode][1]
                count += 1
                if curNode[2] == "Z":
                    break
        counts[node] = count

print(counts)
ans = 1

for count in counts.values():
    ans *= count

print(math.lcm(*counts.values()))

f.close()