# f = open("input.txt", "r")
f = open("test.txt", "r")

lines = [x.strip() for x in f]

digits = "123456789"

val = 0

for line in lines:
    num = ""
    for char in line:
        if char in digits:
            num += char

    final = num[0] + num[len(num) - 1]

    print(final)
    val += int(final)

print(val)

f.close()