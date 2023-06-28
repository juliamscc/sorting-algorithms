def merge(array, left, right):
    i = j = k = 0
    while(i < len(left) and j < len(right)):
        if (left[i] <= right[j]):
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

def mergeSort(array):
    if(len(array) > 1):
        quite = len(array) // 2

        left = array[:quite]
        right = array[quite:]

        mergeSort(left)
        mergeSort(right)
        merge(array, left, right)
    return array