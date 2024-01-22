try: 
    numerator = int(input('Enter a number to divide: '))
    denominator = int(input('Enter a number to divide by: '))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(f'{e}, Cannot divide by zero!')
except ValueError as e:
    print(f'{e}, Numerator and denominator must be numbers!')
else:
    print('The result is {0:.3f}, ({0}).'.format(result))
finally:
    print('This always executes')
    