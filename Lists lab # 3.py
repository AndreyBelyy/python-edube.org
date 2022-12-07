# Your task is to write a program which removes all the number repetitions from the list.
# The goal is to have a list in which all the numbers appear not more than once.
# Note: assume that the source list is hard-coded inside the code - you don't have to enter it from the keyboard.
# Of course, you can improve the code and add a part that can carry out a conversation with the user and obtain all the data from her/him.
# Hint: we encourage you to create a new list as a temporary work area - you don't need to update the list in situ.

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
#
true_list = []
for i in range(len(my_list)): # how many times to do the loop
    if my_list[i] not in true_list: # compare current value with values in new list
        true_list.append(my_list[i]) # add number to new list

print("The list with unique elements only:")
print(my_list)
print(true_list)
