import threading
import time
import main  # Import the standard version code

# Function to divide the workload among multiple threads
def thread_function(start, end, results):
    primes = main.find_primes_in_range(start, end)
    results.extend(primes)

# Divide the range among 4 threads
ranges = [(1, 250000), (250001, 500000), (500001, 750000), (750001, 1000000)]
results = []

# Start time
start_time = time.time()

# Create and start threads
threads = []
for r in ranges:
    t = threading.Thread(target=thread_function, args=(r[0], r[1], results))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

# End time
end_time = time.time()

print(f"Total Number of Primes: {len(results)}")
print(f"Execution time with multithreading: {end_time - start_time:.6f} seconds")
