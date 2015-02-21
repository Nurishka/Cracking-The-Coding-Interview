# Project Euler. Problem 5.
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(number): # passing a number with 0 at the start breaks the code
    num = str(number)
    reversedNum = ""
    for i in xrange(len(num) - 1, -1, -1):
        reversedNum += num[i]

    if reversedNum == num:
        return True
    return False

def findLargestPalindrome():
    largestPalindrome = 0
    for i in xrange(999, 99, -1):
        for j in xrange(999, 99, -1):
            product = i * j
            if product > largestPalindrome and isPalindrome(product):
                largestPalindrome = product

    return largestPalindrome

print findLargestPalindrome()
