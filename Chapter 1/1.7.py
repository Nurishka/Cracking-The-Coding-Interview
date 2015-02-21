# 1.7 Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column is set to 0.

# range(5) -> [0, 1, 2, 3, 4]
# O(n * m) + O(n * m) + O(n * m) = O(3 * n * m) = O(n * m)
# additional memory: O(n + m)
def setToZero(matrix):
    n = len(matrix)
    m = len(matrix[0])
    zerosInRows = [False] * n
    zerosInColumns = [False] * m

    # O(n * m)
    for i in xrange(n):
        for j in xrange(m):
            if matrix[i][j] == 0:
                zerosInRows[i] = True
                zerosInColumns[j] = True
    # O(n * m)
    for row in xrange(n):
        if zerosInRows[row]:
            for col in xrange(m):
                matrix[row][col] = 0

   # O(n * m)
    for col in xrange(m):
        if zerosInColumns[col]:
            for row in xrange(n):
                matrix[row][col] = 0

    return matrix

def unitTest(matrix, expected):
    ans = setToZero(matrix)
    if len(ans) == len(expected) and len(ans[0]) == len(expected[0]):
            for i in xrange(len(ans)):
                for j in xrange(len(ans[0])):
                    if ans[i][j] != expected[i][j]:
                        print "Test failed."
                        return
            print "Test passed."
    else:
        print "Test failed: matrices have different sizes."

inputMatrix = []
expectedMatrix = []

unitTest(inputMatrix, expectedMatrix)
