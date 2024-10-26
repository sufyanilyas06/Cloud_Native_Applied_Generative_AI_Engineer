
var1 = float(input("Enter the first number: "))
var2 = float(input("Enter the second number: "))
op = input("Enter an operator (+, -, *, /): ")


if op == "+":
    result = var1 + var2
    print(f"The sum of {var1} and {var2} is {result}")
elif op == "-":
    result = var1 - var2
    print(f"The difference between {var1} and {var2} is {result}")
elif op == "*":
    result = var1 * var2
    print(f"The product of {var1} and {var2} is {result}")
elif op == "/":
    if var2 != 0:
        result = var1 / var2
        print(f"The division of {var1} by {var2} gives {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator entered.")
