# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Taking user input
try:
    number = int(input("Enter a positive integer: "))
    
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        # Calling the factorial function and displaying the result
        print(f"The factorial of {number} is: {factorial(number)}")

except ValueError:
    print("Please enter a valid integer!")
