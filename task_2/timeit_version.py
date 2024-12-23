import timeit

# Measure the time for the function
execution_time = timeit.timeit('main.find_primes_in_range(1, 1000000)', setup='import main', number=1)

print(f"Execution time using timeit: {execution_time:.6f} seconds")
