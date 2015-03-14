def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print factorial(4) # 24
print factorial(5) # 120
print factorial(6) # 720