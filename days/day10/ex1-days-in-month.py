def is_leap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True

    return False

def days_in_month(year, month):     
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    if month == 2 and is_leap(year):
        return 29

    return month_days[month - 1]

if __name__ == "__main__":
    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))
    if (month < 1 or month > 12) or year < 0:
        print("Invalid value!")
        exit(1)

    print(days_in_month(year, month))
