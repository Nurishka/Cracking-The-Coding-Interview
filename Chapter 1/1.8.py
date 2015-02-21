# 1.8 Assume you have a method isSubstring which checks if one word is a substring of
#another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using
#only one call to isSubstring (i.e., “waterbottle” is a rotation of “erbottlewat”).

# isSubstring("abcccc", "cc") -> True
# isSubstring("aaa", "b") -> False
# s = 'abcd'
# s[0:2] == 'ab'
# len(s) is n, len(t) is m
# O(n * m)
def isSubstring(s, t):
    m = len(t)
    for startIndex in xrange(len(s) - m + 1): # O(n - m) = O(n)
        if s[startIndex:startIndex + m + 1] == t: # not O(1), it's O(m)
            return True

    return False

# given s1 and s2, checks if s2 is the rotation of s1
# s1 = qwerty
# s2 = tyqwer
# a = 'ty', b = 'qwer'
# s1 = ba, s2 = ab,
# s1s1 = baba
# s1 = 'ab', s2 = 'b'
def isRotation(s1, s2):
     return len(s1) == len(s2) and isSubstring(s1 + s1, s2)
