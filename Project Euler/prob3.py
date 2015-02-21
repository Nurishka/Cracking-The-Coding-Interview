#Project Euler. Problem 3.
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def isPrime(number):
    if number == 1:
        return False
    divisor = 2
    while divisor != number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True

def findLargestPrimeFactor(number):
    divisor = 2
    while divisor != number:
        if number % divisor == 0:
            number /= divisor
        else:
            while True:
                divisor += 1
                if isPrime(divisor):
                    break
    
    return divisor
