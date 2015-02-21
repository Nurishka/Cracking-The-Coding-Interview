#1.5 Write a method to replace all spaces in a string with ‘%20’

def replaceWhitespaces(str):
    if (str.count(" ") != 0):
        for num in range(0, str.count(" ")):
            str = str[:str.find(" ")] + "%20" + str[(str.find(" ") + 1):]

    return str

print replaceWhitespaces("Yo, how are you feeling?")
print replaceWhitespaces("           ")
print replaceWhitespaces("haah aah dlkfajdl das  ")
