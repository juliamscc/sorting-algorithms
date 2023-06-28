def straightSelection(array):
    for i in range(len(array)):
        k = i
        min = array[i]
        for j in range(i+1, len(array)):
            if (array[j] < min):
                k = j
                min = array[j]
        array[k] = array[i]
        array[i] = min
    return array