
# Prime Number Check and Number Exploration

This Python script defines a function to check if a number is prime and a main function that explores some predefined favorite numbers. The script will determine if the sum of these favorite numbers is a prime number.

## Code

```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    name = "Alex"
    favorite_numbers = [4, 6, 9]

    print(f"Hello, {name}! Let's explore your favorite numbers:")

    for num in favorite_numbers:
        if num % 2 == 0:
            print(f"The number {num} is even.")
        else:
            print(f"The number {num} is odd.")
        
        square = num ** 2
        print(f"The number {num} and its square: ({num}, {square})")
    
    sum_of_numbers = sum(favorite_numbers)
    print(f"\nAmazing! The sum of your favorite numbers is: {sum_of_numbers}")

    if is_prime(sum_of_numbers):
        print(f"Wow, {sum_of_numbers} is a prime number!")
    else:
        print(f"{sum_of_numbers} is not a prime number.")
```

## How it Works

1. The `is_prime(n)` function checks if a number `n` is a prime number. It uses an efficient method of iterating through potential divisors and returns `True` if `n` is prime, `False` otherwise.
2. The `main()` function:
   - Defines a name and a list of favorite numbers.
   - Iterates through the list to check whether each number is odd or even and computes its square.
   - Calculates the sum of the favorite numbers.
   - Checks if the sum is a prime number using the `is_prime` function and prints the result.

## Example Output

```
Hello, Alex! Let's explore your favorite numbers:
The number 4 is even.
The number 4 and its square: (4, 16)
The number 6 is even.
The number 6 and its square: (6, 36)
The number 9 is odd.
The number 9 and its square: (9, 81)

Amazing! The sum of your favorite numbers is: 19
Wow, 19 is a prime number!
```
