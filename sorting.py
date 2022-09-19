from datetime import datetime
import time
from random import choice


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        item_to_insert = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > item_to_insert:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = item_to_insert
    return arr


def selection_sort(arr):
    for i in range(len(arr)):
        lowest_value_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[lowest_value_index]:
                lowest_value_index = j
        arr[i], arr[lowest_value_index] = arr[lowest_value_index], arr[i]
    return arr


def merge_sort(arr):
    sorted_list = []
    left_list = arr[0:len(arr)//2]
    right_list = arr[len(arr)//2:]
    left_list_index = right_list_index = 0

    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        q = choice(arr)
        L = []
        M = []
        R = []
        for elem in arr:
            if elem < q:
                L.append(elem)
            elif elem > q:
                R.append(elem)
            else:
                M.append(elem)
        return quicksort(L) + M + quicksort(R)


'''List of numbers to sort'''
a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88, -61, -97,
     -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 79, 97, 0,
     -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26, 63,
     -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]

"""Function to translate the class 'datetime.timedelta' to 'float' to further output the time spent on sorting 
in seconds"""


def milliseconds(t):
    t = str(t)
    s = '0'
    s += t[7:]  # Because I used 'time.sleep(1)' I start the line with index 7
    s = float(s) * 1000  # Converting seconds to milliseconds, changing the data type to 'float' from 'str'
    return s


start_time = datetime.now()  # Output time in milliseconds spent on sorting
bubble_sort(a)
time.sleep(1)
print(f'Bubble Sort execution time - {milliseconds(datetime.now() - start_time)} milliseconds')


start_time = datetime.now()
insertion_sort(a)
time.sleep(1)
print(f'Insertion Sort execution time - {milliseconds(datetime.now() - start_time)} milliseconds')

start_time = datetime.now()
selection_sort(a)
time.sleep(1)
print(f'Selection Sort execution time - {milliseconds(datetime.now() - start_time)} milliseconds')

start_time = datetime.now()
merge_sort(a)
time.sleep(1)
print(f'Merge Sort execution time - {milliseconds(datetime.now() - start_time)} milliseconds')

start_time = datetime.now()
quicksort(a)
time.sleep(1)
print(f'Quick Sort execution time - {milliseconds(datetime.now() - start_time)} milliseconds')
