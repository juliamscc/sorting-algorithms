def insertionSort(array):
    for i in range(len(array)):
        j = i
        temp = array[i]
        while(j > 0 and array[j-1] > temp):
            array[j] = array[j-1]
            j -= 1
        array[j] = temp
    return array