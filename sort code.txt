import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    step = 0
    for i in range(n):
        for j in range(0,n-i-1):
            step += 1
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                step += 1
    return step

def selection_sort(arr):
    n = len(arr)
    step = 0
    for i in range(n):
        min_i = i
        step += 1
        for j in range (i+1,n):
            step += 1
            if arr[j] < arr[min_i]:
                min_i = j
                step += 1
        arr[i],arr[min_i] = arr[min_i],arr[i]
        step += 1
    return step

arr = []
step_bubble = []
step_selection = []
size_arr = []
size = 100
x = 10
while x <= size:
    for j in range(x):
        z = int(random.randint(1,99))
        arr.append(z)
    sb = bubble_sort(arr)
    ss = selection_sort(arr)
    step_bubble.append(sb)
    step_selection.append(ss)
    x = x+10

x = 10
while x < 101:
    size_arr.append(x)
    x = x+10


plt.plot(size_arr,step_bubble)
plt.plot(size_arr,step_selection)
plt.show()
