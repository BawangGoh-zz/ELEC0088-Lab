## Part 1) Write a function that receives a list and returns the maximum
## value in that list

## Part 2) Write a function that returns the factorial of a given number. 
## Also attempt this by using a recursive function (a function that calls 
## itself), noting that factorial of n is equal to n times factorial of n-1

## Part 3) Write a function that receives a list and returns a ordered 
## version of that list.

# User input list
def inputList():
    input_string = input("Enter a list of element separate by space\n")
    myList = list(map(int,input_string.split()))
    print(myList)
    return myList

# Return the maximum value in the list
def maxVal(list):
    return max(list)

# Return factorial number using recursive function
def recFactorial(n):
    if n == 0:
        return 1
    elif n < 0:
        print("Error no negative value factorial")
    else:
        return n*recFactorial(n-1)

# Return the ordered list
def orderList(list):
    newList = list.copy()
    newList.sort()
    return newList

def main():
    # Part 1)
    list1 = inputList()
    max_value = maxVal(list1)
    print(max_value)

    # Part 2)
    integer = int(input("Enter an integer value\n"))
    factorial = recFactorial(integer)
    print(factorial)

    # Part 3) 
    list2 = inputList()
    sortedList = orderList(list2)
    print(sortedList)

if __name__ == "__main__":
    main()