# A natural number is prime if it is greater than 1 and has no divisors other than 1 and itself.

# Complicated? Not at all. For example, 8 isn't a prime number,
# as you can divide it by 2 and 4 (we can't use divisors equal to 1 and 8, as the definition prohibits this).

# On the other hand, 7 is a prime number, as we can't find any legal divisors for it.


# Your task is to write a function checking whether a number is prime or not.
check_number = int(input("Number to check, please: "))
def is_prime(num):
    #
    # Write your code here.
    #
    for x in range(2, num):
        if num % x == 0:
            print("It is not prime number.")
            return False

        else:
            print("Prime number is " + str(num))
            return True
print(is_prime(check_number))

