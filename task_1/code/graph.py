import matplotlib.pyplot as plt

# List of Python flavors
flavors = ['CPython', 'PyPy', 'Jython', 'MicroPython']

# Time in seconds
times = [0.001529, 0.015046, 0.041000, 0.006702]

# Create a bar chart with different colors and a smaller canvas size
plt.figure(figsize=(8, 4))  # Set the figure size to be smaller
colors = ['skyblue', 'lightgreen', 'coral', 'orchid']  # Define colors for each bar

plt.bar(flavors, times, color=colors)

# Add labels and title
plt.xlabel('Python Flavors')
plt.ylabel('Execution Time (seconds)')
plt.title('Performance Comparison of Factorial Calculation')

# Show the graph
plt.show()
