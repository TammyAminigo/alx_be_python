# match_case_calculator.py

# Ask the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask for the operation
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation using match case
match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
            exit()
        result = num1 / num2
    case _:
        print("Invalid operation selected.")
        exit()

# Convert 50.0 → 50, but keep decimals like 3.5
if float(result).is_integer():
    result = int(result)

print(f"The result is {result}.")

