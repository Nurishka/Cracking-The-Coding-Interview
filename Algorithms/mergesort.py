# [9, 1, 83, 2, 7, 21, 37, 22]
# 5//2 -> 2, 4//2 -> 2, 9/4 -> 2
def merge_sort(a):
    n = len(a)
    if n > 1:
        middleIndex = n//2
        left = a[:middleIndex]
        right = a[middleIndex:]
        left = merge_sort(left)
        right = merge_sort(right)
        a = merge(left, right)
    return a

# a = [1, 3, 9], b = [2, 83], res = [1, 2, 3, 9, 83]
# time complexity - O(n + m) + O(n) + O(m) = O(2n + 2m) = O(2 * (n + m)) = O(n + m)
def merge(a, b):
    i = 0
    j = 0
    k = 0
    n = len(a)
    m = len(b)
    res = [-1] * (n + m)
    while i < n and j < m:
        if a[i] < b[j]:
            res[k] = a[i]
            i += 1
        else:
            res[k] = b[j]
            j += 1
        k += 1
    # process the remainder
    while i < n:
        res[k] = a[i]
        i += 1
        k += 1
    while j < m:
        res[k] = b[j]
        j += 1
        k += 1

    return res

myArr = [9, 1, 83, 2, 7, 21, 37, 22]
print merge_sort(myArr)