'''given sa number, check if it is an armstrong number or not'''
# Function to check if a number is an Armstrong number
def is_armstrong_number(number):
    # Convert the number to a string to easily access each digit
    num_str = str(number)
    # Calculate the number of digits
    num_digits = len(num_str)
    # Initialize sum to 0
    sum_of_powers = 0
    # Calculate the sum of each digit raised to the power of the number of digits
    for digit in num_str:
        sum_of_powers += int(digit) ** num_digits
    # Check if the sum of powers is equal to the original number
    return sum_of_powers == number
number = input("Enter a number: ")
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")