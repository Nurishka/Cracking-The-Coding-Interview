# Quicksort method 1
def qsort(arr):
     if len(arr) <= 1:
          return arr
     else:
          return qsort([x for x in arr[1:] if x<arr[0]]) + [arr[0]] + qsort([x for x in arr[1:] if x>=arr[0]])


# Quicksort method 2
from random import randint

def quicksort(v):
    n = len(v)
    if n > 1:
        pivotIndex = randint(0, n - 1) # O(1)
        less, equal, greater = partition(v, pivotIndex) # O(n)
        return quicksort(less) + equal + quicksort(greater)
    return v

def partition(v, pivotIndex):
    less = []
    equal = []
    greater = []
    for i in xrange(len(v)):
        if v[i] > v[pivotIndex]:
            greater.append(v[i])
        elif v[i] == v[pivotIndex]:
            equal.append(v[i])
        else:
            less.append(v[i])

    return (less, equal, greater)

myArr = [9, 1, 83, 21, 2, 7, 21, 37, 22]
print qsort(myArr)
print quicksort(myArr)