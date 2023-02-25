import sys
sys.path.insert(0, '/home/student/Documents/210962092/Lab2')
from Q1 import *

def cycles(nodes, i, v, stack):
	v[i] = True
	stack[i] = True
	for j in nodes[i].edges:
		if not v[j.edge[1]]:
			if cycles(nodes,j.edge[1],v,stack):
				return True
		elif stack[j.edge[1]]:
			return True
	stack[i] = False
	return False

def isCyclic(nodes):
	v = [False]*len(nodes)
	stack = [False]*len(nodes)
	for i in range(len(nodes)):
		if not v[i]:
			if cycles(nodes,i,v,stack):
				return True
	return False

nodes=[]
for i in range(4):
	nodes = nodes  + [Node(i)]
nodes[0].addEdge( nodes[2], isDirected = True)
nodes[2].addEdge( nodes[0], isDirected = True)
nodes[0].addEdge( nodes[1], isDirected = True)
nodes[1].addEdge( nodes[2], isDirected = True)
nodes[2].addEdge( nodes[3], isDirected = True)
nodes[3].addEdge( nodes[3], isDirected = True)
print(isCyclic(nodes))