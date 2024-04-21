import time
import random
import copy
import math
# Function to find the partition position
def partition(array, low, high):
 
    # choose the rightmost element as pivot
    pivot = array[high]
 
    # pointer for greater element
    i = low - 1
 
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
# function to perform quicksort
 
 
def quickSort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)

def sort_q(array, size):
    quickSort(array, 0, size - 1)


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
 
 
def mergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
        
def sort_m(array, size):
    mergeSort(array, 0, size-1)
def timing():
    experiment_size = 1000
    array_size = 100000
    quick_sort_times = []
    merge_sort_times = []
    for i in range(experiment_size):
        arr_merge_sort = generate_random(array_size)
        arr_quick_sort = copy.deepcopy(arr_merge_sort)
        timer = Timer()
        
        timer.start_timer()
        sort_m(arr_merge_sort, array_size)
        timer.end_timer()
        merge_sort_times.append(timer.get_elapsed_time())
        

        timer.start_timer()
        sort_q(arr_quick_sort, array_size)
        timer.end_timer()
        quick_sort_times.append(timer.get_elapsed_time())
    mean_quick_sort = get_mean(quick_sort_times, experiment_size)
    mean_merge_sort = get_mean(merge_sort_times, experiment_size)
    
    var_quick_sort = get_var(mean_quick_sort,quick_sort_times, experiment_size)
    var_merge_sort = get_var(mean_merge_sort, merge_sort_times, experiment_size)
    print("Results: ----------")
    print("Mean of quick sort: ", mean_quick_sort)
    print("Mean of merge sort: ", mean_merge_sort)
    print("Variance of quick sort: ", var_quick_sort)
    print("Variance of merge sort: ", var_merge_sort)
    f = open("results.csv" ,"w")
    f.write("Trial,Quick sort data,Merge Sort Data,,Quick sort mean,Merge sort mean,Quick sort variance, Merge sort variance\n")
    f.write(str(1) +","+str(quick_sort_times[0]) + "," + str(merge_sort_times[0]) + ", ," + str(mean_quick_sort) + "," + str(mean_merge_sort) + "," + str(var_quick_sort) + "," + str(var_merge_sort) + "\n")
    for i in range(1, experiment_size):
        f.write(str(i+1) +","+str(quick_sort_times[i]) + "," + str(merge_sort_times[i]) + "\n")
    f.close()


def get_mean(arr, experiment_size):
    sum = 0
    for element in arr:
        sum = sum + element
    return sum / experiment_size
def get_var(mean, arr, experiment_size):
    sum = 0
    for element in arr:
        sum += pow((element-mean),2)
    return sum/(experiment_size -1)

class Timer():
    def __init__(self):
        self.delta_time = 0
        self.start_time = 0
    def start_timer(self):
        self.start_time = time.time()
    def end_timer(self):
        if (self.start_time) == 0:
            return "timer not started"
        self.delta_time = (time.time() - self.start_time)
        self.start_time = 0
    def get_elapsed_time(self):      
        return self.delta_time
    

def generate_random(size):
    return [random.randint(0, 100000) for i in range(size)]
timing()
