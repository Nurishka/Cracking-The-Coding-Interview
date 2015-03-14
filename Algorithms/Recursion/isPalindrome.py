def isPalindrome(str):
    n = len(str)
    if n <= 1:
        return True

    if str[0] == str[n - 1]:
        return isPalindrome(str[1:n - 1])
    else:
        return False

print isPalindrome("xyzzyx")
print isPalindrome("motor")
print isPalindrome("rotor")
print isPalindrome("alimannamilakdjfadlfqwepiqp")