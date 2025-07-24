# Simple calculator
# Asking the user to input two numbers

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# Asking the user to choose an operation 
print("Choose an operation: +, -, *, /")
operation = input("Enter your operation: ")

# Performing the calculation
if operation == '+':
    result = num1 + num2
    print("Result:", result)

elif operation == '-':
    result = num1 - num2
    print("Result:", result)

elif operation == '*':
    result = num1 * num2
    print("Result:", result)

elif operation == '/':
    if num2 != 0:
        result = num1 /num2
        print("Result:", result)
    else:
        print("Error: cannot divide by zero.")

else:
    print("Invalid operation. Please choose +, -, *, /.")