# Simple Calculator

def calculator():
    print("Simple Calculator")
    
    # Input: two numbers and an operation
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    print("Select operation: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    operation = input("Enter your choice (1/2/3/4): ")

    # Perform the calculation
    if operation == '1':
        result = num1 + num2
        print(f"The result of addition is: {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"The result of subtraction is: {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"The result of multiplication is: {result}")
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of division is: {result}")
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid operation choice.")

# Run the calculator function
calculator()
