# In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis
# (it still remains unproven) which can be described in the following way:

# take any non-negative and non-zero integer number and name it c0;
# if it's even, evaluate a new c0 as c0 ÷ 2;
# otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
# if c0 ≠ 1, skip to point 2.
# The hypothesis says that regardless of the initial value of c0, it will always go to 1.

# Write a program which reads one natural number and
# executes the above steps as long as c0 remains different from 1.
# We also want you to count the steps needed to achieve the goal.
# Your code should output all the intermediate values of c0, too.

n = int(input("Your number, please: "))
steps = 0

while n != 1:
    if n % 2 == 0: # check if number is even
        n /= 2
        steps += 1 # add count to step
        print(int(n))
    else: # if number is odd
        n = 3 * n + 1
        steps += 1
        print(int(n))

print("Steps = " + str(steps))
