import datetime

date1 = datetime.datetime(2019, 5, 28)
date2= datetime.datetime(2019, 7, 18)

def is_in_semester(month, day):
    date3 = datetime.datetime(2019, month, day)
    return date3

def main():
    date_input = str(input("Ente Your date in mm/dd firmate: "))
    month = int(date_input.split('/')[0])
    day = int(date_input.split('/')[1])
    date = is_in_semester(month, day)
    print("Input date between in 5/28 - 7/28: ", date1 < date < date2)

if __name__ == "__main__":
    main()
