
def quicksort(array, low, high):
    if low < high:
        pivot_location = partition(array, low, high)
        quicksort(array, low, pivot_location)
        quicksort(array, pivot_location + 1, high)

def partition(array, low, high):
    pivot = array[low]
    pivot_index = low

    while low < high:
        while low < len(array) and array[low] <= pivot:
            low += 1
        while array[high] > pivot:
            high -= 1

        if low < high:
            array[low], array[high] = array[high], array[low]

    array[high], array[pivot_index] = array[pivot_index], array[high]
    return high

list = [34, 56, 12, 98, 1, 74, 7, 23, 3, 9]
quicksort(list, 0, len(list) - 1)

print(f"sorted array = {list}")



def quick(array, low, high): # on first iteration, low = start of list, high = end of list
    if low < high:
        pivot_location = part(array, low, high)
        quicksort(array, low, pivot_location)
        quicksort(array, pivot_location + 1, high)

def part(array, low, high):
    i = low
    j = high
    pivot = array[low]
    pivot_index = i
    while i < j:
        while i < len(array) and array[i] <= pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i < j:
            