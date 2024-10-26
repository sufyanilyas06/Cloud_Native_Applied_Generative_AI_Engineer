<div align="center">
    <h1> Basic Calculator </h1>
 </div>

## step1:
First we will take data in **var1** & **var2** variable using **input** funtion  and specified there data type with **float** keyword. After that we will take opeartor in **op**

```python
var1 = float(input("Enter the first number: "))
var2 = float(input("Enter the second number: "))
op = input("Enter an operator (+, -, *, /): ")

```
## Step2:
Now at this stage we will check what type of opeator is enter by the user and perform calculation accordingly. Finally answer will be shown on screen using **print** funtion, which we stored in **result** variable.

```python
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
    
```
## Output:
Enter the first number: 2  
Enter the second number: 4  
Enter an operator (+, -, *, /): *  
The product of 2.0 and 4.0 is 8.0  

