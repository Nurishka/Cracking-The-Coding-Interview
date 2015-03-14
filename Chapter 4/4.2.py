# 4.2
# Given a directed graph, design an algorithm to find out whether there is a route between
# two nodes.
# Graph assumed to be represented in an adjacency list
def bfs(graph, s, t): # route from s to t
    numV = len(graph)
    visited = [False] * numV
    visited[s] = True
    queue = [s]

    while len(queue) != 0:
        curV = queue.pop(0)

        for i in xrange(len(graph[curV])):
            nextV = graph[curV][i]
            if not visited[nextV]:
                visited[nextV] = True
                queue.append(nextV)


    return visited[t]

def doesRouteExist(graph, a, b):
    return bfs(graph, a, b) or bfs(graph, b, a)

# http://www.seas.gwu.edu/~simhaweb/alg/lectures/module7/figures/g32.gif
graph = [
    [1],
    [2],
    [0, 3, 5],
    [4, 6],
    [6],
    [3, 7],
    [3],
    []
]

print doesRouteExist(graph, 4, 2)
print doesRouteExist(graph, 6, 7)
print doesRouteExist(graph, 2, 6)