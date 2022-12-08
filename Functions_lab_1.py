# Your task is to write and test a function which takes one argument (a year)
# and returns True if the year is a leap year, or False otherwise.
year = int(input("Year, please: "))
month = int(input("Month, please: "))


def is_year_leap(year):
    if year % 4 == 0:
        a = True
    else:
        a = False
    return (a)


vys_year = is_year_leap(year)


# Part 2

def days_in_month(year, month):
    lm = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year < 1582 or month < 1 or month > 12:
        return None
    if month == 2 and vys_year == True:
        month = 29
    else:
        month = lm[month - 1]
    return year, month


print(days_in_month(year, month))
