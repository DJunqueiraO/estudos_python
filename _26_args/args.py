# This code defines a function called sum_numbers that 
# takes any number of arguments and returns the sum of 
# those numbers. It initializes a variable result to 0, 
# converts the input to a list, sets the first element to 0, 
# and then iterates through the list, adding each number 
# to the result.
def sum_numbers(*numbers):
    result = 0
    numbers = list(numbers)
    numbers[0] = 0
    for number in numbers:
        result += number
    return result

print(sum_numbers(2,3,4,5,6))