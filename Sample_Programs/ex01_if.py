#example_if.py
"""Compare integers using if statements and comparison operators"""

print("Enter the Two Number will show you the comparison")

# read the first integer
number1 = int(input("Enter first number:" ))

# read the Second number
number2 = int(input("Enter second number:" ))

if number1 == number2:
    print(number1, 'is equal to', number2)
if number1 != number2:
    print(number1, 'is not equal to', number2)
if number1 > number2:
    print(number1, 'is greater than', number2)
if number1 < number2:
    print(number1, 'is less than', number2)
if number1 >= number2:
    print(number1, 'is greater than or equal to ', number2)
if number1 <= number2:
    print(number1, 'is less than or equal to', number2)