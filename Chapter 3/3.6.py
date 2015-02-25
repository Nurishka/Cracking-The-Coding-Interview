# 3.6
# Write a program to sort a stack in ascending order. You should not make any assumptions
# about how the stack is implemented. The following are the only functions that
# should be used to write this program: push | pop | peek | isEmpty.

import sys

class Stack(object):
    def __init__(self, data=[]): # data is an array
        self.data = data

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def isEmpty(self):
        return len(self.data) == 0

    def getStack(self): # only for testing
        return self.data

def swap(array, firstIndex, secondIndex):
    buf = array[firstIndex]
    array[firstIndex] = array[secondIndex]
    array[secondIndex] = buf

def findIndexofMinInSubarray(array, startIndex):
    minVal = array[startIndex]
    minIndex = startIndex
    for i in xrange(startIndex, len(array), 1):
        if array[i] < minVal:
            minVal = array[i]
            minIndex = i
    return minIndex

def selSort(array):
    for i in xrange(len(array)):
        swap(array, findIndexofMinInSubarray(array, i), i)

    return array

def sortStack(stack):
    if stack.isEmpty():
        return stack

    sortedArr = []
    while not stack.isEmpty():
        sortedArr.append(stack.peek())
        stack.pop()
    sortedArr = selSort(sortedArr)

    resStack = Stack()
    for num in sortedArr:
        resStack.push(num)

    return resStack

myStack = Stack()
myStack.push(3)
myStack.push(5)
myStack.push(1)
myStack.push(2)
myStack.push(6)
myStack.push(6)
myStack.push(91)
myStack.push(6)
myStack.push(83)
myStack.push(92)
myStack.push(238)
myStack.push(192)
myStack.push(0)
myStack.push(-2)
print sortStack(myStack).getStack()

# sortStack(myStack)
# print myStack.getStack()
# also works, why?
