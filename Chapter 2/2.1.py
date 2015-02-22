# 2.1 Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class linkedList(object):
    def __init__(self, head=None):
        self.head = head

    # node becomes the head of the list
    def insert(self, node):
        if self.head:
            node.nextNode = self.head
            self.head = node
        else:
            self.head = node

    # data = 7
    # [1, 2, 4, 8]
    # Omega(n) <= Theta(n) <= O(n)
    def search(self, data):
        if self.head:
            node = self.head
            while node != None:
                if node.data == data:
                    return node
                node = node.nextNode
        raise ValueError('Data not in the list')

def removeDuplicates1(linkedList): # removes duplicates by storing all the data in an array
    nums = []
    node = linkedList.head
    lastNode = None
    while (node != null):
        isFound = False
        for i in xrange(len(nums)):
            if nums[i] == node.data:
                lastNode.nextNode = node.nextNode # remove the node by referencing the last node to the next one
                isFound = True
        if not isFound:
            nums.append(node.data)
        lastNode = node
        node = node.nextNode

    return linkedList

def removeDuplicates2(linkedList): # removes duplicates without a buffer
    prevNode = linkedList.head
    curNode = prev.next
    while cur != None:
        runner = linkedList.head
        while runner != curNode:
            if runner.data == curNode.data:
                prevNode.next = curNode.next
                prevNode = curNode
                curNode = curNode.next
                break # all duplicates were removed, there's no point to search further
            else:
                runner = runner.next

    return linkedList
