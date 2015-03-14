# graph - adjacency list
# graph = [[], [], [], [], []]
# find the shortest distance between s and t
def bfs(graph, s, t):
    n = len(graph) # number of nodes in graph
    queue = []
    queue.append(s)
    dist = [-1] * n # dist[i] - distance between s to i
    dist[s] = 0
    while len(queue) != 0:
        cur = queue.pop(0) # del queue[0]
        for i in xrange(len(graph[cur])):
            next = graph[cur][i]
            if dist[next] == -1:
                dist[next] = dist[cur] + 1
                queue.append(next)
    return dist[t]

graph = [
    [1],
    [0, 4, 5],
    [3, 4, 5],
    [2, 6],
    [1, 2],
    [1, 2, 6],
    [3, 5],
    []
]

expected = [4, 3, 1, 0, 2, 2, 1, -1]
for i in xrange(len(graph)):
    if bfs(graph, 3, i) == expected[i]:
        print "Test passed!"
    else:
        print "Test failed, returned distance: %i, expected: %i" % (bfs(graph, 3, i), expected[i])
