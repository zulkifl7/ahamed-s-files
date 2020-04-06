import datetime

date1 = datetime.date(1939, 1, 9)
date2 = datetime.date(1945, 2, 9)

def is_within(month, day, year):
    date = datetime.date(year, month, day)
    if year == 1939 or year == 1945:
        a = date1 < date < date2
    elif 1940 < year < 1944:
        a = True
    else:
        a = False
    return a
    
def main():
    date_input = input("Enter date in mm/dd/yyyy format: ")
    month = int(date_input.split ('/')[0])
    day = int(date_input.split('/')[1])
    year = int(date_input.split('/')[2])
    date3 = is_within(month, day, year)
    print("Input date between in 1939-1945: ",  date3)
if __name__ == "__main__":
    main()
