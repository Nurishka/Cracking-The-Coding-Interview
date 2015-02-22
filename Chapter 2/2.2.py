# 2.2 Implement an algorithm to find the nth to last element of a singly linked list

def findElement(linkedList, n):
    node = linkedList.head
    if node == None:
        raise ValueError("The linked list is empty.")
    lenList = 1
    while node != None:
        node = node.next
        lenList += 1
    targetElement = lenList - n - 1
    if targetElement >= 0:
        node = linkedList.head
        for i in xrange(targetElement):
            node = node.next
    else:
        raise ValueError("The nth to last element is out of range.")

    return node
