import datetime

def julian(day, month, year):
    daynum = 31 * (month - 1) + day
    if month > 2:
        daynum -= (4 * month + 23)//10
        if year % 4 == 0:
            daynum += 1
    return daynum
def main():
    day = int(input("Enter the day: "))
    month = int(input("Enter the month: "))
    year = int(input("Enter the year: "))
    print(julian(day, month, year))
    print(year)

if __name__ == '__main__':
    main()
