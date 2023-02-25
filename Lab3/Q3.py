import sys
sys.path.insert(0, '/home/student/Documents/210962092/Lab2')
from Q1 import *

def maze(nodes, i, v, stack, dest, start):
	v[i] = True
	for j in nodes[i].edges:
		if not v[j.edge[1]] and not v[dest]:
			maze(nodes,j.edge[1],v,stack,dest,start)
	if v[dest] and i!=start:
		stack.append(i)
def go(nodes, start = 2, dest=20):
	v = [False]*len(nodes)
	stack = []
	maze(nodes,2,v,stack, dest, start)
	print(stack[::-1]+ [start])

nodes = []
for i in range(21):
	nodes = nodes  + [Node(i)]
nodes[1].addEdge( nodes[2], isDirected = False)
nodes[1].addEdge( nodes[6], isDirected = False)
nodes[2].addEdge( nodes[3], isDirected = False)
nodes[3].addEdge( nodes[8], isDirected = False)
nodes[8].addEdge( nodes[7], isDirected = False)
nodes[6].addEdge( nodes[11], isDirected = False)
nodes[11].addEdge( nodes[12], isDirected = False)
nodes[12].addEdge( nodes[17], isDirected = False)
nodes[17].addEdge( nodes[16], isDirected = False)
nodes[17].addEdge( nodes[18], isDirected = False)
nodes[18].addEdge( nodes[19], isDirected = False)
nodes[19].addEdge( nodes[14], isDirected = False)
nodes[14].addEdge( nodes[13], isDirected = False)
nodes[14].addEdge( nodes[9], isDirected = False)
nodes[9].addEdge( nodes[10], isDirected = False)
nodes[10].addEdge( nodes[5], isDirected = False)
nodes[5].addEdge( nodes[4], isDirected = False)
nodes[10].addEdge( nodes[15], isDirected = False)
nodes[15].addEdge( nodes[20], isDirected = False)
go(nodes, 20)