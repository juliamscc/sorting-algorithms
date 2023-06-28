def swap(array, a, b):
    [array[a], array[b]] = [array[b], array[a]]

def createArrayIndex(array):
    arrayIndex = []
    for i in range(len(array)):
        arrayIndex.append(i)
    return arrayIndex

def partition(array, arrayIndex, left, right):
    pivot = array[(right + left) // 2]
    while(left <= right):
        while(array[left] < pivot):
            left += 1
        while(array[right] > pivot):
            right -= 1
        if(left <= right):
            swap(array, left, right)
            swap(arrayIndex, left, right)
            left += 1
            right -= 1
    return left

def quick(array, arrayIndex, left, right):
    if(len(array) > 1):
        index = partition(array, arrayIndex, left, right)
        if(left < index-1):
            quick(array, arrayIndex, left, index-1)
        if(index < right):
            quick(array, arrayIndex, index, right)

def quickSort(array):
    arrayIndex = createArrayIndex(array)
    quick(array, arrayIndex, 0, len(array)-1)
    return array