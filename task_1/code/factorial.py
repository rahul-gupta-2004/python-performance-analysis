import time

# Define the factorial function using recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Record the start time
start_time = time.time()

# Define the range for calculating factorials
n = 100

# Calculate the factorial of each number up to n
for i in range(n):
    factorial(n)

# Print a message indicating the range of factorials calculated
print("Factorial calculated of each number from 1 to ", n)

# Record the end time
end_time = time.time()

# Calculate and print the execution time
execution_time = end_time - start_time
print("Execution time: {:.6f} seconds".format(execution_time))

