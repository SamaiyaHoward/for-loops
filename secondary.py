# -------------------- Section 2 -------------------- #

# ---------- Part 1 | Patterns ---------- #
print(
    '>> Section 2\n'
    '>> Part 1\n'
)

# 1 - for Loop | Patterns
#   a. Prompt input from the user in the form of a symbol. Save to a variable named s.
#   b. Prompt input from the user in the form of an integer. Save to a variable named size.
#   a. Create the following pattern using a for loop, and the symbol and size provided by the user.
#
# Example Output (need help)
#
#   >> symbol... $
#   >> size... 4
#
#   $$$$ | sp = 1 | sym = 4 | sym + 1 = sp
#    $$$ | sp = 2 | sym = 3 | sym + 1 = sp
#     $$ | sp = 3 | sym = 2 | sym + 1 = sp
#      $ | sp = 4 | sym = 1 | sym + 1 = sp
#
# Write Code Below #
one = 1
s = input('enter a symbol: ')
size = int(input('enter a number for the size: '))
for i in range(size,0,-1):
    print(' ' * (size - i + 1) + (s * i))


# 2 - for Loop | Patterns
#   a. Prompt input from the user in the form of a symbol. Save to a variable named s.
#   a. Create the following pattern using a for loop, and the symbol and size provided by the user.
#
# Example Output
#
#   >> symbol... $
#
#   $$$$$
#   $$$$
#   $$$
#   $$
#   $
#   $$
#   $$$
#   $$$$
#   $$$$$
#
#
# Write Code Below #
s = input('enter a symbol: ')
size = int(input('size >> '))
for i in range(size,0,-1):
    print(s * i)
for i in range(2,size + 1,1):
    print(s * i)
print()
print('different methods'.upper())
print()
start = -size
stop = size
step = 1
for i in range(start, stop, step):
    print(s * (abs(i) + 1))


# 3 - for Loop | Patterns
#   a. Prompt input from the user in the form of a symbol. Save to a variable named s.
#   a. Create the following pattern using a(two) for loop(s), and the symbol and size provided by the user.
#
# Example Output
#
#   >> symbol... $
#
#   $
#   $$
#   $$$
#   $$$$
#   $$$$$
#   $$$$
#   $$$
#   $$
#   $
#
#
# Write Code Below #
s = input('symbol >> ')
size = int(input('size >> '))
for i in range(1,size):
    print(i * s)
for f in range(size,0,-1):
    print(f * s)

# ---------- Part 2 | Mathematical Patterns ---------- #
print(
    '>> Section 2\n'
    '>> Part 2\n'
)

# 1 - for Loop | Sum n
#   a. Prompt input from the user in the form of an integer. Save to a variable named n.
#   b. Calculate the sum of all numbers between 0 and n, and print the value.
#
#   sum = n + n - 1 + n - 2 + n - 3
#
#   EXAMPLE: 5 --> 5 + 4 + 3 + 2 + 1
#
# Example Output
#
#   >> n = 10
#   >> 55
#
# Write Code Below #

# 0 --> 0 + 1 = 1 --> 1 + 2 = 3 --> 3 + 3

n = int(input('enter a number: '))
sum1 = 0

for i in range(n, 0, -1):
    sum1 += i
    print(sum1)
    
print(sum1)

# 1 - for Loop | n!
#   a. Prompt input from the user in the form of an integer. Save to a variable named n.
#   b. Calculate n! using loops.
#
#   n! or n factorial is equal to n * (n - 1) * (n - 2) * ... * 1
#
#   EXAMPLE: 5 --> 5 * 4 * 3 * 2 * 1
#
#
# Example Output
#
#   >> n = 10
#   >> 3628800
#
# Write Code Below #
n = int(input('enter a number: '))
sum1 = 1

for i in range(n, 0, -1):
    sum1 *= i
    print(sum1)