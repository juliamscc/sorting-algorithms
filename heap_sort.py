def swap(array, a, b):
    [array[a], array[b]] = [array[b], array[a]]

def heapify(array, size, i):
    largest = i  
    left = 2 * i + 1
    right = 2 * i + 2

    if left < size and array[largest] < array[left]:
        largest = left
    if right < size and array[largest] < array[right]:
        largest = right
    if largest != i:
        swap(array, i, largest)
        heapify(array, size, largest)

def heapSort(array):
    size = len(array)
    for i in range(size//2 - 1, -1, -1):
        heapify(array, size, i)

    for i in range(size-1, 0, -1):
        swap(array, i, 0)
        heapify(array, i, 0)
    return array