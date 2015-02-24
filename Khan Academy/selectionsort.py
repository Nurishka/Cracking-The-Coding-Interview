# implementation of selection sort
def swap(array, firstIndex, secondIndex):
    buf = array[firstIndex]
    array[firstIndex] = array[secondIndex]
    array[secondIndex] = buf

def findIndexofMinInSubarray(array, startIndex):
    minVal = array[startIndex]
    minIndex = startIndex
    for i in xrange(startIndex, len(array), 1):
        if array[i] < minVal:
            minVal = array[i]
            minIndex = i
    return minIndex

def selSort(array):
    for i in xrange(len(array)):
        swap(array, findIndexofMinInSubarray(array, i), i)

    return array

myarr = [0, 10, 912, 19, 91, 81, 28, 29, 93, -1, -235]
print selSort(myarr)
