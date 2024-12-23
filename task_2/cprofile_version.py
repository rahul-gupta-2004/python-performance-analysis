import cProfile  # Import cProfile for profiling
import main  # Import the main.py module

# Run cProfile on the main function from main.py
cProfile.run('main.find_primes_in_range(1, 1000000)')
