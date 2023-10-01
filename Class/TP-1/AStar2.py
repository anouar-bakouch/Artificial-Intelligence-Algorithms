# A* algorithm

class Node:

    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic

class Graph:

    def __init__(self, graph):
        self.graph = graph

    def successors(self, node):
        return self.graph[node]

    def heuristic(self, node):
        return node.heuristic

    def cost(self, node1, node2):
        successors = self.successors(node1)
        for (n, w) in successors:
            if n == node2:
                return w
        return 0

    def neighbors(self, node):
        voisins = []
        for (n, w) in self.successors(node):
            voisins.append(n)
        return voisins

    def goal(self, node, goal):
        return node == goal

    def addEdge(self, node1, node2, weight):
        self.graph[node1].append((node2, weight))

    def AStar(self, start, end):
        open = []
        closed = []
        open.append(start)
        start.parent = None
        path = []
        
        while True :
            # if open is empty, return failure
            if len(open) == 0:
                return None
            
            # choose the node with the lowest f on the open list
            current = open[0]
            open.remove(current)
            closed.append(current)

            # if goal(node) return path 
            if self.goal(current, end): 
                while current.parent != None:
                    path.append(current)
                    current = current.parent
                path.append(start)
                return path[::-1] 

            # for each successor of current
            for node in self.neighbors(current):
                # if node in closed list, continue
                if node in closed:
                    continue
                # if node not in open list, add it
                if node not in open:
                    node.parent = current
                    open.append(node)
                # else if the cost of current + cost of current to node < cost of node
                else:
                    if self.cost(current, node) < self.cost(node.parent, node):
                        node.parent = current
                        open.append(node)

        
# TEST 
A = Node('A',3)
B = Node('B',2)
C = Node('C',7)
D = Node('D',5)
E = Node('E',1)
F = Node('F',2)
G = Node('G',0)
H = Node('H',0)

# C is the start bc h = 0
# H is the goal bc h = 0

graph = {
    C:[(A,2),(B,1)],
    A:[(B,4),(D,3),(C,2)],
    B:[(D,3),(E,7),(F,1),(A,4),(C,1)],
    D:[(E,2),(F,1),(B,3),(A,3)],
    E:[(F,1),(D,2),(B,7)],
    F:[(G,1),(H,1),(E,1),(D,1),(B,1)],
    G:[(H,1),(F,1)],
    H:[(G,1),(F,1)]
}

g = Graph(graph)
goal = g.AStar(C,H)
print(f"path : {[node.name for node in goal]}")