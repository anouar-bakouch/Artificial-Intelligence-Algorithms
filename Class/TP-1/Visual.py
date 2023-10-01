import matplotlib.pyplot as plt
import random

class Node:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic

A = Node('A',3)
B = Node('B',2)
C = Node('C',9)
D = Node('D',5)
E = Node('E',1)
F = Node('F',2)
G = Node('G',0)
H = Node('H',0)

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

# Create a dictionary to store the node positions.
node_positions = {}
for node in graph.keys():
    node_positions[node] = (random.random(), random.random())

# Create a plot and add the nodes.
fig, ax = plt.subplots()
for node, position in node_positions.items():
    ax.plot(position[0], position[1], marker="o", color="blue")
    ax.text(position[0], position[1], node.name +f" (h : {node.heuristic})", ha="right", va="top",color="green", fontsize=12, fontweight="bold")

# Add the edges between the nodes.
for node, neighbors in graph.items():
    for neighbor, cost in neighbors:
        ax.plot([node_positions[node][0], node_positions[neighbor][0]], [node_positions[node][1], node_positions[neighbor][1]], color="blue")

# add the cost to the edge 
for node, neighbors in graph.items():
    for neighbor, cost in neighbors:
        ax.text((node_positions[node][0] + node_positions[neighbor][0])/2, (node_positions[node][1] + node_positions[neighbor][1])/2, cost, ha="right", va="top",color="red", fontsize=12, fontweight="bold")


# Set the labels and title.
ax.set_title("Graph")
plt.axis('off')
plt.title("Graph Representation - Anouar Bakouch", fontsize=15)
plt.tight_layout()
plt.savefig("graph.png", format="PNG")

# size of the figure
fig.set_size_inches(10, 10)
# center of the window
fig.canvas.manager.window.wm_geometry("+%d+%d" % (500, 100))




# Show the plot.
plt.show()

