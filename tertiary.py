# -------------------- Section 3 -------------------- #

# ---------- Part 1 | Patterns ---------- #
print(
    '>> Section 3\n'
    '>> Part 1\n'
)

# 1 - for Loop | Patterns
#   Create a function that will calculate and print the first n numbers of the fibonacci sequence.
#       n is specified by the user.
#
#   NOTE: You can assume that the user will enter a number larger than 2
#
# Example Output
#
#   >> size... 6
#
#   1, 1, 2, 3, 5, 8
#
# Write Code Below #

# using variables, keep track of the last two numbers
# once you've calculated the next number, then you adjust the last two numbers

n = int(input('enter the size limit: '))
num = 1
for i in range(num):
    n += 1
    print(i + n)