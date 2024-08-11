import time
import random
import matplotlib.pyplot as plt

# Bubble Sort implementation
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Selection Sort implementation
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Function to measure the time taken by a sorting algorithm
def time_sort(sort_func, arr):
    start_time = time.time()
    sort_func(arr.copy())
    end_time = time.time()
    return end_time - start_time

# Generating the data for the graph
sizes = list(range(100, 1100, 100))
bubble_sort_times = []
selection_sort_times = []

for size in sizes:
    arr = random.sample(range(size*10), size)
    bubble_sort_times.append(time_sort(bubble_sort, arr))
    selection_sort_times.append(time_sort(selection_sort, arr))

# Plotting the time complexity graph
plt.figure(figsize=(10, 6))
plt.plot(sizes, bubble_sort_times, label='Bubble Sort', marker='o')
plt.plot(sizes, selection_sort_times, label='Selection Sort', marker='o')
plt.title('Time Complexity of Bubble Sort vs Selection Sort')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.legend()
plt.grid(True)
plt.show()
