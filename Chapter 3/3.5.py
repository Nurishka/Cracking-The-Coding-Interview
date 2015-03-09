# implementation of a  stack
class Stack(object):
    def __init__(self, data=[]): # data is an array
        self.data = data

    def push(self, value):
        if value < self.minimum():
            newNode = Node(value, value)
        else:
            newNode = Node(value, self.minimum())
        self.data.append(newNode)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    # returns minimum in O(1)
    def minimum(self):
        if len(self.data) > 0:
            return self.peek().getMinimum()
        else:
            return sys.maxint

#{3} -> value = 3, minimum = 3
#{5, 3} -> value = 5, minimum = 3
class Node(object):
    def __init__(self, value, minimum):
        self.value = value
        self.minimum = minimum

    def getMinimum(self):
        return self.minimum

class myQueue(object):
# have one stack 
