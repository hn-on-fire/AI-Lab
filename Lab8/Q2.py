from BFS import *
if __name__ == "__main__":
    nodes = []
    for i in range(9):
        nodes = nodes  + [Node(i)]
    nodes[0].addEdge( nodes[1], 15)
    nodes[0].addEdge( nodes[4], 15)
    nodes[0].addEdge( nodes[2], 2)
    nodes[1].addEdge( nodes[5], 10)
    nodes[2].addEdge( nodes[6], 3)
    nodes[3].addEdge( nodes[4], 10)
    nodes[3].addEdge( nodes[8], 75)
    nodes[4].addEdge( nodes[8], 35)
    nodes[5].addEdge( nodes[8], 5)
    nodes[5].addEdge( nodes[0], 1)
    nodes[5].addEdge( nodes[7], 25)
    nodes[6].addEdge( nodes[3], 5)
    nodes[7].addEdge( nodes[8], 0)
    h= {0:45,1:30,2:40,3:60,4:10,5:35,6:35,7:0,8:0}
    print(BFS(nodes,0,[7,8],h))