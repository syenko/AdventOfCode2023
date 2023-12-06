f = open("input.txt", "r")
# f = open("test.txt", "r")

lines = [x.strip() for x in f]

ans = 1

time = int("".join(lines[0].split(": ")[1].split()))
dist = int("".join(lines[1].split(": ")[1].split()))

def check(num):
    return (num) * (time - num) < dist

# find max value w/ binary search
left = 0
right = time
while left < right-1:
    mid = (left + right) // 2
    if check(mid):
        right = mid
    else:
        left = mid

a_max = left

# find min value with binary search
left = 0
right = time
while left < right-1:
    mid = (left + right) // 2
    if check(mid):
        left = mid
    else:
        right = mid

a_min = right

print(a_max - a_min + 1)

f.close()