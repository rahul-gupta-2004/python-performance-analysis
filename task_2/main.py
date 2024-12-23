import math
import time

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Function to find primes in a given range
def find_primes_in_range(start, end):
    primes = []
    for num in range(start, end):
        if is_prime(num):
            primes.append(num)
    return primes

# Define the range to search for prime numbers
start = 1
end = 1000000

# Start time
start_time = time.time()

# Find primes in the range
primes = find_primes_in_range(start, end)

# End time
end_time = time.time()

# Print the total number of prime numbers and the execution time
print(f"Total number of primes in range({start}, {end}): {len(primes)}")
print(f"Execution time: {end_time - start_time:.6f} seconds")
