class Queue(object):
    def __init__(self, data=None): # data is an array
        self.data = data

    def enqueue(data):
        self.data.append(data)

    def dequeue(data):
        self.data.pop[0]

    def getFront():
        return self.data[0]

    def getBack():
        return self.data[-1]

class Vertex(object):
    __init__(self, )

def doBFS(graph, source):



adjList = [
    [1],
    [0, 4, 5],
    [3, 4, 5],
    [2, 6],
    [1, 2],
    [1, 2, 6],
    [3, 5],
    []
    ];
bfsInfo = doBFS(adjList, 3)
for i in xrange(len(adjList)):
    print ("vertex" + i + ": distance = " + bfsInfo[i].distance)
