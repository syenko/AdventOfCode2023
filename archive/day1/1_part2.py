f = open("input.txt", "r")
# f = open("test.txt", "r")

lines = [x.strip() for x in f]


digits = "123456789"
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

val = 0

for line in lines:
    nums = []
    sub = ""
    for char in line:
        # check if current character is a digit (numerical)
        if char in digits:
            nums.append(char)
            sub = ""
        else:
            sub += char

        # check if any of the spelled out numbers can be found in the current substring
        for num in numbers:
            if num in sub:
                nums.append(str(numbers.index(num) + 1))
                # keep the last character in case there is overlap (threeight -> 38)
                sub = sub[len(sub) - 1]

    final = nums[0] + nums[len(nums) - 1]

    val += int(final)

print(val)

f.close()