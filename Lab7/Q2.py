from Astar import *
import sys
sys.path.insert(0, '/home/student/Documents/210962092/Lab2')
from Q1 import *


if __name__ == "__main__":
    nodes = []
    for i in range(10):
        nodes = nodes  + [Node(i)]
    nodes[0].addEdge( nodes[1], 5, isDirected = True)
    nodes[0].addEdge( nodes[4], 6, isDirected = True)
    nodes[1].addEdge( nodes[2], 3, isDirected = True)
    nodes[1].addEdge( nodes[7], 9, isDirected = True)
    nodes[2].addEdge( nodes[1], 2, isDirected = True)
    nodes[2].addEdge( nodes[3], 1, isDirected = True)
    nodes[3].addEdge( nodes[0], 6, isDirected = True)
    nodes[3].addEdge( nodes[8], 5, isDirected = True)
    nodes[3].addEdge( nodes[6], 7, isDirected = True)
    nodes[4].addEdge( nodes[0], 1, isDirected = True)
    nodes[4].addEdge( nodes[3], 2, isDirected = True)
    nodes[4].addEdge( nodes[5], 2, isDirected = True)
    nodes[5].addEdge( nodes[9], 7, isDirected = True)
    nodes[6].addEdge( nodes[4], 2, isDirected = True)
    nodes[6].addEdge( nodes[9], 8, isDirected = True)
    h= {0:5,1:7,2:3,3:4,4:6,5:5,6:6,7:0,8:0,9:0}
    print(Astar(nodes,0,[7,8,9],h))