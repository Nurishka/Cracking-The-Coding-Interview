# Project Euler. Problem 5.
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def findNumber(): # extremely inefficient
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
