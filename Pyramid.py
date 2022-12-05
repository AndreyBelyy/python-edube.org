# Task
# Your task is to write a program which reads the number of blocks the builders have,
# and outputs the height of the pyramid that can be built using these blocks.
# Note: the height is measured by the number of fully completed layers -
# if the builders don't have a sufficient number of blocks and cannot complete the next layer,
# they finish their work immediately.

bu = 0 # block used per level
l = 0 # number of levels
b = int(input("Number of blocks. please: "))

if b < 0:
    print("No it's antimaterial")

elif b > 0:
    while (b - bu) > 0: # if blocks number - blocks used  more than zero (means we have enough blocks for next level)
      bu += 1 # each level requires one more block
      b -= bu # each level requires blocks
      l += 1 # levels count

print(l)
