# **Performance Analysis of Python Implementations & Algorithm Parallelization**

This repository contains two key projects that explore the performance of Python implementations and the impact of algorithm parallelization. The objective is to analyze execution times, measure efficiency, and identify optimal methods for faster computation.

---

## **Project 1: Performance Analysis of Python Implementations**

### **Introduction**

This project evaluates the performance of different Python implementations using a **Factorial Calculation** program. By comparing the execution time for calculating factorials from 1 to 100, the project highlights the speed differences between Python flavors. The goal is to determine which implementation performs best for recursive computations.

### **Python Flavors Used**

1. **CPython**: The default and most widely used Python interpreter.
2. **PyPy**: A Python interpreter with Just-In-Time (JIT) compilation, designed to speed up Python code.
3. **Jython**: A Python implementation that runs on the Java Virtual Machine (JVM).
4. **MicroPython**: A lightweight Python interpreter for embedded devices and microcontrollers.

Each flavor was tested in a **virtual environment** to ensure isolated execution. The execution time was recorded, and performance was visualized using bar charts.

---

## **Project 2: Algorithm Parallelization**

### **Introduction**

This project focuses on optimizing a **Prime Finder Algorithm** using parallelization techniques. The aim is to demonstrate how execution time can be reduced by using multi-threading, multi-processing, and profiling tools. Different methods were applied to analyze the program's performance and scalability, with a focus on the benefits of parallel computation.

### **Methods Used**

1. **Standard Version**: A basic single-threaded implementation to establish a baseline for performance.
2. **cProfile Analysis**: Used to profile the code and identify performance bottlenecks.
3. **Timeit Analysis**: Used to measure precise execution time for specific code blocks.
4. **Multithreading**: Multiple threads work simultaneously to find prime numbers, but due to Python's GIL (Global Interpreter Lock), this method is less effective.
5. **Multiprocessing**: Uses multiple processes to run tasks in parallel, bypassing GIL restrictions. The program was tested with 2, 4, 6, and 8 processes to observe scalability.

The execution time for each method was recorded and visualized using bar charts. The analysis highlights how multiprocessing can significantly reduce execution time, especially for CPU-bound tasks like prime number calculation.

---

With these two projects, this repository demonstrates a **comprehensive analysis of Python performance** and **the benefits of parallelization techniques**. The methods and tools used in both projects provide valuable insights into how developers can optimize their Python programs for speed and efficiency.
