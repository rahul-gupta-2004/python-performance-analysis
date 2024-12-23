import multiprocessing
import time
import main  # Import the standard version code

# Function to divide the workload among multiple processes
def process_function(start, end):
    return main.find_primes_in_range(start, end)

# List of processor counts to test
processors = [2, 4, 6, 8]

for p in processors:
    start_time = time.time()
    
    # Divide the range into equal parts for each processor
    ranges = [(i * 1000000 // p + 1, (i + 1) * 1000000 // p) for i in range(p)]
    with multiprocessing.Pool(p) as pool:
        results = pool.starmap(process_function, ranges)
        
    end_time = time.time()
    
    total_primes = sum(len(res) for res in results)
    print(f"Processors: {p}, Total Primes: {total_primes}, Execution Time: {end_time - start_time:.6f} seconds")
