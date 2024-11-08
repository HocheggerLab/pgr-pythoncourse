# Step 1: Define what a prime number is
# A prime number is a number greater than 1 that has no divisors other than 1 and itself.
# Examples of prime numbers: 2, 3, 5, 7, 11, 13, ...

# Step 2: Get user input
# Ask the user to input a number to check if it's prime.
# Convert the input to an integer and store it in a variable.

# Step 3: Handle edge cases
# Check if the number is less than or equal to 1.
# If so, print that the number is not prime (since prime numbers must be greater than 1).

# Step 4: Initialize the check
# For numbers greater than 1, we need to check if the number is divisible by any number other than 1 and itself.

# Step 5: Loop through potential divisors
# Use a loop to test divisibility from 2 up to the square root of the number.
# If the number is divisible by any of these, it is not prime.
# You can use the modulo operator (%) to check if there is no remainder when dividing by a potential divisor.

# Step 6: Determine if the number is prime
# If the loop completes without finding any divisors, the number is prime.
# If a divisor is found, the number is not prime.

# Step 7: Output the result
# After checking, print whether the number is prime or not.

# Step 8: Optional enhancement – check multiple numbers
# You could extend the program to allow the user to check multiple numbers or input a range of numbers.