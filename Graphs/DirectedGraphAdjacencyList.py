from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def createEdge(self,v1,v2):
        self.graph[v1].append(v2)


    def printGraph(self):
        for node in self.graph:
            for v in self.graph[node]:
                print (node," => ",v )

g = Graph()
g.createEdge(1,5)
g.createEdge(1,100)
g.createEdge(5,2)
g.createEdge(2,7)
g.createEdge(7,1)

print("The Directed Graph using adjacency List is - ")
g.printGraph()
    