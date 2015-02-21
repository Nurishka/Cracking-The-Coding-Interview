# Binary Search Implementation

def searchFor(num, numbers):
    min = 0
    max = len(numbers) - 1
    while (max >= min):
        avg = int((min + max) / 2)
        if (numbers[avg] == num):
            return avg
        else:
            if (num > numbers[avg]):
                min = avg + 1
            else:
                max = avg - 1

    return -1

nums = [0, 13, 19, 24, 29, 32, 48, 51, 53, 68, 72, 74, 81, 87, 93, 97]

def unit_test(num, numbers, expected):
    if (searchFor(num, numbers) == expected):
        print "Test passed."
    else:
        print "Test failed for number: %i, got an index of %i, expected: %i" % (num, searchFor(num, numbers), expected)

unit_test(68, nums, 9)
unit_test(0, nums, 0)
unit_test(97, nums, 15)
