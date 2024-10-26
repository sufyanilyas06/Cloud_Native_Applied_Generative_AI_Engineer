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