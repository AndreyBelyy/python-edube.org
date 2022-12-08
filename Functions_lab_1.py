# Your task is to write and test a function which takes one argument (a year)
# and returns True if the year is a leap year, or False otherwise.

def is_year_leap(year):
    if year % 4 == 0:
        a = True
    else:
        a = False
    return(a)
# put your code here
#
print(is_year_leap(2024))