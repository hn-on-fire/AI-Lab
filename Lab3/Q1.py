import sys
sys.path.insert(0, '/home/student/Documents/210962092/Lab2')
from Q1 import *
def tsr(nodes, i, v, stack):
	v[i] = True
	for j in nodes[i].edges:
		if not v[j.edge[1]]:
			tsr(nodes,j.edge[1],v,stack)
	stack.append(i)
def ts(nodes):
	v = [False]*len(nodes)
	stack = []
	for i in range(len(nodes)):
		if not v[i]:
			tsr(nodes,i,v,stack)
	print(stack[::-1])

nodes = []
for i in range(6):
	nodes = nodes  + [Node(i)]
nodes[2].addEdge( nodes[3], isDirected = True)
nodes[3].addEdge( nodes[1], isDirected = True)
nodes[4].addEdge( nodes[1], isDirected = True)
nodes[4].addEdge( nodes[0], isDirected = True)
nodes[5].addEdge( nodes[2], isDirected = True)
nodes[5].addEdge( nodes[0], isDirected = True)
ts(nodes)

