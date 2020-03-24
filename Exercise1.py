## Part 1) Ask user to input 3 numbers and prints the biggest number
## Part 2) Ask two numbers representing a month and a year and then print
## the number of days that month has
def inputNum():
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    num3 = float(input("Third number: "))
    return num1,num2,num3

def compareNum(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

def dateTime():
    month = int(input("Which month "))
    year = int(input("Which year "))
    return month, year

# Define leap year
def leap_year(year):
    if (year % 4 == 0):
        return True
    else:
        return False

# February for leap year
def checkFeb(dict, year):
    if(year % 4 == 0):
        dict["2"] = 29
    return dict

def main():
    num1, num2, num3 = inputNum()
    print(compareNum(num1, num2, num3))

    # Defining dictionary (very similar to database) keys to search the days in the months
    days_in_months = {"1": 31, "2": 28, "3": 31, "4": 30,
                "5": 31, "6": 30, "7": 31, "8": 31,
                "9": 30, "10": 31, "11": 30, "12": 31}

    month, year = dateTime()
    days_in_months = checkFeb(days_in_months, year)
    print("Total days: " + str(days_in_months[str(month)]) + " in " + str(month) + " " + str(year))

if __name__ == "__main__":
    main()