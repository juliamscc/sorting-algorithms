# def shellSort(alist):
#     sublistcount = len(alist)//2
#     while sublistcount > 0:

#         for startposition in range(sublistcount):
#             gapInsertionSort(alist,startposition,sublistcount)

#         print("After increments of size",sublistcount, "The list is",alist)

#         sublistcount = sublistcount // 2

# def gapInsertionSort(alist,start,gap):
#     for i in range(start+gap,len(alist),gap):

#         currentvalue = alist[i]
#         position = i

#         while position>=gap and alist[position-gap]>currentvalue:
#             alist[position]=alist[position-gap]
#             position = position-gap

#         alist[position]=currentvalue

# alist = [25, 57, 48, 37, 12, 92, 86, 33]
# shellSort(alist)
# print(alist)


def swap(array, a, b):
    [array[a], array[b]] = [array[b], array[a]]

def shellSort(array, gap=0):
    for i in range(gap):
        currentValue = array[i]
        position = i

        while position >= gap and array[position - gap] > currentValue:
            swap(array, position, position-gap)
            position =position - gap
        array[position] = currentValue
    return array

# void shell_sort(int v[], int n{
# int i, j, h, aux;
# h = 1;
# while (h<n/3)
# h = 3*h+1;
# while (h>0){

# for (i=h;i<n;i++){
# aux = v[i];
# j = i;
# while(j>=h && aux <v[j-h]){

# v[j] = v[j-j]
# j = j-h;

# }
# v[j]=aux

# }
# h = (h-1)/3;
# }