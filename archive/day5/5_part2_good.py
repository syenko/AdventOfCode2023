f = open("input.txt", "r")
# f = open("test.txt", "r")

lines = [x.strip() for x in f]

ans = 0

seeds = [int(x) for x in lines[0].split(": ")[1].split()]

class Range():
    def __init__(self, second, first, length, start=False, end=False, offset=False):
        self.start = first
        self.end = first + length
        self.offset = second - first

        if start: self.start = start
        if end: self.end = end
        if offset: self.offset = offset

    def __repr__(self):
        return "Range {}-{} off: {}".format(self.start, self.end, self.offset)

    def inRange(self, num):
        return self.start <= num < self.end

    def convert(self, num):
        return num + self.offset

    def bisect(self, o_range):
        # intersect
        if o_range.start < self.end + self.offset and o_range.end > self.start + self.offset:
            new_start = max(o_range.start, self.start + self.offset)
            new_end = min(o_range.end, self.end + self.offset)
            new_offset = self.offset + o_range.offset
            return Range(0,0,0,start=new_start - self.offset, end=new_end - self.offset, offset=new_offset)


seed_ranges = [Range(seeds[x], seeds[x], seeds[x + 1]) for x in range(0, len(seeds), 2)]

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
# read in ranges
while i < len(lines):
    line = lines[i]
    if len(line.strip()) == 0:
        cur += 1
        i += 2
        continue

    [start, end, length] = [int(x) for x in line.split()]

    vals[cur].append(Range(start, end, length))

    i += 1

cur_ranges = seed_ranges[:]
new_ranges = []
for i in range(len(vals)):
    for r in cur_ranges:
        start = r.start
        end = r.end
        range_list = []

        for next_map in vals[i]:
            bis = r.bisect(next_map)
            # print(r, next_map)
            # print(bis)
            if bis:
                new_ranges.append(bis)
                if bis.start <= start:
                    start = bis.end
                    continue
                if bis.end >= end:
                    end = bis.start
                    continue
                range_list.append(bis.start)
                range_list.append(bis.end)

        if end > start:
            range_list.append(start)
            range_list.append(end)
            range_list.sort()

            new_ranges.extend(
                [
                    Range(
                        0,0,0,
                        start=range_list[i],
                        end=range_list[i+1],
                        offset=r.offset
                    ) for i in range(0,len(range_list), 2)
                ]
            )

    cur_ranges = new_ranges[:]
    print(cur_ranges)
    new_ranges = []

print(cur_ranges)

ans = 100000000000
for r in cur_ranges:
    ans = min(r.start + r.offset, ans)

print(ans)

f.close()