# Write a method to decide if two strings are anagrams or not.

def isAnagram1(a, b):
    return sorted(a) == sorted(b)
