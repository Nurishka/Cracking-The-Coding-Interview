# Project Euler. Problem 5.
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Method 1
def findNumber1(): # brute forcing
    num = 1
    while True:
        dividesToAll = True
        for i in xrange(11, 21, 1)
            if num % i != 0:
                dividesToAll = False
                break
        if dividesToAll:
            break
        num += 1
    return num

print findNumber()
"""
# Method 2
def primes(n): # returns an array of primes to n
    res = []
    for i in xrange(2, n + 1, 1):
        isPrime = True
        for j in xrange(2, i, 1):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            res.append(i)
    return res
    # 35 = 5 * 7
    # 28 = 2 * 2 * 7

def primeFactorization(num, primeList):
    primeFactors = []
    i = 0
    while i != (len(primeList) - 1):
        if num % primeList[i] == 0:
            primeFactors.append(primeList[i])
            num /= primeList[i]
        else:
            i += 1
    return primeFactors

def findLeastCommonMultiple(num1, num2):
    if num1 == 0 or num2 == 0 or type(num1) != int or type(num2) != int:
        return "LCM can be only found for positive integers"

    if num1 > num2:
        primeList = primes(num1)
    else:
        primeList = primes(num2)

    primeFactorsNum1 = primeFactorization(num1, primeList)
    primeFactorsNum2 = primeFactorization(num2, primeList)
    lcm = 1
    for prime in primeList:
        if primeFactorsNum1.count(prime) > primeFactorsNum2.count(prime):
                lcm *= prime ** primeFactorsNum1.count(prime)
        else:
            lcm *= prime ** primeFactorsNum2.count(prime)
    return lcm

def findNumber2():
    i = 2
    num = findLeastCommonMultiple(i, i - 1)
    while i < 20:
        num = findLeastCommonMultiple(num, i + 1)
    return num
"""
