# given an array A, find all triplets (a, b, c) s.t. a + b + c == target
# A = [-5, -3, 18, -10, 7, 9, 15, 0, 0, 5], target = 15
# [-5, 15, 5], [-3, 18, 0], [15, 0, 0]
# a + b + ? = target => c = target - (a + b)
# c(n, k) = n!/k!(n-k)!
# triplets = c(n, 3)

# O(n^2)
def findTriplet1(A, target):
    n = len(A)
    used = {}
    for i in xrange(n):
        if A[i] in used:
            used[A[i]] += 1
        else:
            used[A[i]] = 1

    for i in xrange(0, n):
        for j in xrange(i + 1, n):
            c = target - (A[i] + A[j])
            used[A[i]] -= 1
            used[A[j]] -= 1
            if c in used and used[c] > 0:
                print A[i], A[j], c
            used[A[i]] += 1
            used[A[j]] += 1

# O(n * logn) + O(n^2 * logn) = O(n^2 * logn)
def findTriplet2(A, target):
    A.sort() # O(nlogn)
    n = len(A)
    for i in xrange(0, n):
        for j in xrange(i + 1, n): # O(n^2)
            c = target - (A[i] + A[j])
            cIndex = binarySearch(A, c) # O(logn)
            if cIndex != -1:
                print A[i], A[j], c

def binarySearch(a, target):
    n = len(a)
    L = 0
    R = n - 1
    while L <= R:
        mid = (L + R) // 2
        if a[mid] == target:
            return mid
        elif a[mid] > target:
            R = mid - 1
        else:
            L = mid + 1
    return -1

# O(n^3)
def findTriplet3(A, target):
    res = []
    n = len(A)
    for i in xrange(0, n):
        for j in xrange(i + 1, n):
            for k in xrange(j + 1, n):
                if A[i] + A[j] + A[k] == target:
                    res.append([A[i], A[j], A[k]])
    print res

# target = 567
# return the index of the target, otherwise: -1

myArr = [-5, -3, 18, -10, 7, 9, 15, 0, 0, 5, 7]
print findTriplet3(myArr, 15)
