# computing powers of a number
def numberToPower(x, n):
    if n == 0:
        return 1

    if n > 0 and n % 2 == 0:
        sqrtX = numberToPower(x, n / 2)
        return sqrtX * sqrtX

    if n > 0 and n % 2 == 1:
        return x * numberToPower(x, n - 1)

    if n < 0:
        return 1 / float(numberToPower(x, -n))

print numberToPower(2, 6)
print numberToPower(5, -3)
print numberToPower(3, 3)
print numberToPower(2, 50)