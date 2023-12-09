f = open("input.txt", "r")
# f = open("test.txt", "r")

lines = [x.strip() for x in f]

ans = 0

for line in lines:
    nums = [int(x) for x in line.split()]
    vals = [nums[:]]
    while nums.count(0) != len(nums):
        vals.append([nums[x + 1] - nums[x] for x in range(len(nums) - 1)])
        nums = vals[len(vals) - 1][:]

    sol = sum([val[len(val) - 1] for val in vals])

    # print(vals)
    # print(sol)

    ans += sol


print(ans)

f.close()