# Problem 6. Project Euler.
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def findSumOfSquares(n):
    res = 0
    for i in xrange(1, n + 1, 1):
        res += i ** 2
    return res

def findSquareOfSum(n):
    res = 0
    for i in xrange(1, n + 1, 1):
        res += i
    res ** 2
    return res

def difference(n):
    return abs(findSumOfSquares(n) - findSquareOfSum(n))

print difference(100)
