# Let's imagine the following problem:
#
# you need a program to evaluate the students' average scores;
# the program should ask for the student's name, followed by her/his single score;
# the names may be entered in any order;

# entering an empty name finishes the inputting of the data
# (note 1: entering an empty score will raise the ValueError exception,
# but don't worry about that now, you'll see how to handle such cases
# when we talk about exceptions in the second part of the Python Essentials course series)

# a list of all names, together with the evaluated average score, should be then emitted.


school_class = {}

while True:
    name = input("Student's name, please: ")
    if name == '':
        break
    ocenka = int(input("Ocenki, pojaluista: "))
 #   if ocenka not in range(0, 11):
    if ocenka < 0 or ocenka > 10:
        break

    if name in school_class:
        school_class[name] += (ocenka, )
    else:
        school_class[name] = (ocenka, )
for name in school_class:
    count = 0
    ocenki = 0
    for ocenka in school_class[name]:
        ocenki += ocenka
        count += 1
    print(name, ":", (ocenki / count) )

print(school_class)
