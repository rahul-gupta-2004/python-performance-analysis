import matplotlib.pyplot as plt

# Data for the graph
methods = [
    'Standard', 
    'cProfile', 
    'Timeit', 
    'Multithreading (4 Threads)', 
    'Multiprocessing (2 Processors)', 
    'Multiprocessing (4 Processors)', 
    'Multiprocessing (6 Processors)', 
    'Multiprocessing (8 Processors)'
]

execution_times = [
    5.641796,  # Standard
    5.824426,  # cProfile
    5.487442,  # Timeit
    6.550390,  # Multithreading (4 Threads)
    4.137661,  # Multiprocessing (2 Processors)
    3.346900,  # Multiprocessing (4 Processors)
    3.424486,  # Multiprocessing (6 Processors)
    3.141621   # Multiprocessing (8 Processors)
]

# Colors for each method
colors = [
    'skyblue',     # Standard (single color)
    'lightcoral',  # cProfile
    'lightcoral',  # Timeit
    'gold',        # Multithreading
    'lightgreen',  # Multiprocessing (2 Processors)
    'lightgreen',  # Multiprocessing (4 Processors)
    'lightgreen',  # Multiprocessing (6 Processors)
    'lightgreen'   # Multiprocessing (8 Processors)
]

# Create the bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(methods, execution_times, color=colors)

# Add labels and title
plt.xlabel('Methods Used')
plt.ylabel('Execution Time (seconds)')
plt.title('Performance Comparison of Prime Finder Using Different Methods')

# Rotate x-axis labels for better readability
plt.xticks(rotation=30, ha='right')

# Display the execution time above each bar
for bar, time in zip(bars, execution_times):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 0.1, f'{time:.4f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Show the graph
plt.tight_layout()  # Adjust layout to prevent label cutoff
plt.show()
