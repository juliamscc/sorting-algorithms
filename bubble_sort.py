def swap(array, a, b):
    [array[a], array[b]] = [array[b], array[a]]

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if(array[j] > array[j+1]):
                swap(array, j, j+1)
    return array