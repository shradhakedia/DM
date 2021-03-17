#GRAPH: a-b-c-d-e-a
from collections import defaultdict
from class_queue import Queue
from class_stack import Stack 
class Graph:
    def __init__(self):
        self.edges=defaultdict(list)
    def addedge(self,a,b):
        self.edges[a].append(b)
    def BFS(self,source):
        visitvertex=set()
        queue=Queue(10)
        visitvertex.add(source)
        queue.enqueue(source)
        while not queue.isempty():
            k = queue.dequeue()
            print(k, end = ' ')
            for v in self.edges[k]:
                if v not in visited:
                    visited.add(v)
                    queue.enqueue(v)
        print()

