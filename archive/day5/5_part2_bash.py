f = open("input.txt", "r")
# f = open("test.txt", "r")

lines = [x.strip() for x in f]

ans = 0

seeds = [int(x) for x in lines[0].split(": ")[1].split()]
seed_ranges = [(seeds[x], seeds[x + 1]) for x in range(0,len(seeds),2)]

class Range():
    def __init__(self, second, first, length):
        self.start = first
        self.end = first + length
        self.offset = second - first

    def __repr__(self):
        return "Range {}-{} off: {}".format(self.start, self.end, self.offset)

    def inRange(self, num):
        return self.start <= num < self.end

    def convert(self, num):
        return num + self.offset


seed_to_soil = []
soil_to_fert = []
fert_to_water = []
wat_to_lig = []
lig_to_temp = []
temp_to_hum = []
hum_to_loc = []

vals = [seed_to_soil, soil_to_fert, fert_to_water, wat_to_lig, lig_to_temp, temp_to_hum, hum_to_loc]

cur = 0
i = 3
while i < len(lines):
    line = lines[i]
    if len(line.strip()) == 0:
        cur += 1
        i += 2
        continue

    [start, end, length] = [int(x) for x in line.split()]

    vals[cur].append(Range(start, end, length))

    i += 1

locs = []
for seed_range in seed_ranges:
    for seed in range(seed_range[0], seed_range[0] + seed_range[1]):
        val = seed
        for i in range(len(vals)):
            for r in vals[i]:
                if r.inRange(val):
                    val = r.convert(val)
                    break
        locs.append(val)


print(locs)

print(min(locs))

f.close()