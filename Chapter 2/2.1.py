# 2.1 Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None
