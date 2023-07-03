def shellSort(array, gap = 1):
    for  i  in range(gap):
        gapInsertionSort(array, i, gap)
    return array

def gapInsertionSort(array,start,gap):
    for i in range(start+gap,len(array),gap):

        currentvalue = array[i]
        position = i

        while position>=gap and array[position-gap]>currentvalue:
            array[position]=array[position-gap]
            position = position-gap

        array[position]=currentvalue