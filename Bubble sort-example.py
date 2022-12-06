my_list = [8, 10, 6, 2, 4]  # list to sort

for i in range(len(my_list) - 1):  # we need (5 - 1) comparisons
    if my_list[i] > my_list[i + 1]:  # compare adjacent elements
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # If we end up here, we have to swap the elements.




my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.

while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)


my_list = [879, 76, 91, 198, 5]

swapped = True

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
      if my_list[i] > my_list[i + 1]:
        swapped = True
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)


my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)






# repetition

numbers = []
swapped = True
num = int(input("Quantity of numbers: "))

for i in range(num):
    val = int(input("Numbers, please: "))
    numbers.append(val)

while swapped:
    swapped = False
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            swapped = True
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
print(numbers)

easy = [9, 199, 1876, 1220]
easy.sort()
print(easy)











