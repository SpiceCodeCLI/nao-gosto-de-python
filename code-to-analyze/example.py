import random

# Function to calculate the sum of squares
def sum_of_squares(n):
    sum = 0
    for i in range(1, n+1):
        sum += i * i  # Squaring the number and adding to sum
    return sum

# Function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i  # Multiplying each number to get factorial
    return result

# Random number generator function
def randomize(n):
    return random.randint(0, n-1)  # Generate a random number between 0 and n-1

# Main program
num = 10
random_num = randomize(num)

print(f"Random Number: {random_num}")
print(f"Sum of squares up to {num}: {sum_of_squares(num)}")
print(f"Factorial of {num}: {factorial(num)}")

# Using random number to generate a weird result
weird_result = sum_of_squares(random_num) + factorial(random_num)
print(f"Weird result using random number: {weird_result}")
