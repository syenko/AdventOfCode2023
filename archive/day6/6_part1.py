f = open("input.txt", "r")
# f = open("test.txt", "r")

lines = [x.strip() for x in f]

ans = 1

times = [int(x) for x in lines[0].split(": ")[1].split()]
dists = [int(x) for x in lines[1].split(": ")[1].split()]

for i, time in enumerate(times):
    dist = dists[i]
    works = []
    for j in range(time):
        if j * (time - j) > dist:
            works.append(j)

    r = (max(works)-min(works) + 1)
    ans *= r
print(ans)

f.close()