f = open("input.txt", "r")
# f = open("test.txt", "r")

lines = [x.strip() for x in f]


digts = "123456789"

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

val = 0

for line in lines:
    nums = []
    sub = ""
    for char in line:
        if char in digts:
            nums.append(char)
            sub = ""
        else:
            sub += char

        for num in numbers:
            if num in sub:
                nums.append(str(numbers.index(num) + 1))
                sub = sub[len(sub) - 1]

    final = nums[0] + nums[len(nums) - 1]

    print(final)
    val += int(final)

print(val)

f.close()