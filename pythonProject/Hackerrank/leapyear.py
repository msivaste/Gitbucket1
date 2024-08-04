def is_leap(year):
    leap = True
    noleap = False
    if (year%4==0):
        return leap
    else:
        return noleap

year = int(input())
result = is_leap(year)
print(result)


def is_leap(year):
    leap = False
    #Year divided by 4 is leap year, but need to check if it is not a century year which means not divisible by 100
    if (year % 4 == 0) and (year % 100 != 0):
        leap = True
    #Year divisible by 4 + divisible by 400, then it is leap year
    elif (year%4==0) and (year%400==0):
        leap = True
    return leap

year = int(input())
print(is_leap(year))