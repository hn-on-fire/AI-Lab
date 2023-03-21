import sys
sys.path.insert(0, '/home/student/Documents/210962092/Lab2')
from Lab7.Astar import *
from queue import PriorityQueue
q = PriorityQueue()
def Astar(nodes,start, end, h):
    ret = []
    v = [0]*len(nodes)
    q.put((h[start],(start,0,[start])))
    n = None
    while not q.empty():
        n = q.get()
        #print(n)
        for e in nodes[n[1][0]].edges:
            if not v[e.edge[1]]:
                cost  = e.weight+n[1][1]
                q.put((cost +h[e.edge[1]], (e.edge[1],cost,n[1][2] + [e.edge[1]])))
        v[n[1][0]] = True;
        if n[1][0] in end:
            break
    return n[1][2] if n[1][0] in end else None  


if __name__ == "__main__":
    nodes = []
    for i in range(10):
        nodes = nodes  + [Node(i)]
    nodes[0].addEdge( nodes[1], 6)
    nodes[0].addEdge( nodes[5], 3)
    nodes[1].addEdge( nodes[2], 3)
    nodes[1].addEdge( nodes[3], 2)
    nodes[2].addEdge( nodes[3], 1)
    nodes[2].addEdge( nodes[4], 5)
    nodes[3].addEdge( nodes[4], 8)
    nodes[4].addEdge( nodes[9], 5)
    nodes[4].addEdge( nodes[8], 5)
    nodes[5].addEdge( nodes[6], 1)
    nodes[5].addEdge( nodes[7], 7)
    nodes[6].addEdge( nodes[8], 3)
    nodes[7].addEdge( nodes[8], 2)
    nodes[8].addEdge( nodes[9], 3)
    h= {0:10,1:8,2:5,3:7,4:3,5:6,6:5,7:3,8:1,9:0}
    print(Astar(nodes,0,[9],h))