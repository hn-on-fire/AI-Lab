#uniform cost search

class priorityQ:
	def __init__(self):
		self.q = []
	def enqueue(self,element,cost):	
		for i in range(len(self.q)):
			if(self.q[i][1]>cost):
				self.q.insert(i,(element,cost))
				return 
		self.q.insert(len(self.q),(element,cost))
	def dequeue(self):
		return self.q.pop(0)

import sys
sys.path.insert(0, '/home/student/Documents/210962092/Lab2')
from Q1 import *

def go(s, g, n):
	visited= []
	q = priorityQ()
	q.enqueue(s,0)
	while  len(q.q)!=0:
		v = q.dequeue()
		if v[0] == g:
			return v[1]
		for e in n[v[0]].edges:
			q.enqueue(e.edge[1],v[1]+e.weight)
nodes = []
for i in range(7):
		nodes = nodes  + [Node(i)]
nodes[0].addEdge( nodes[1],2, isDirected = True)
nodes[0].addEdge( nodes[3],5, isDirected = True)
nodes[3].addEdge( nodes[1],5, isDirected = True)
nodes[1].addEdge( nodes[6],1, isDirected = True)
nodes[3].addEdge( nodes[6],6, isDirected = True)
nodes[3].addEdge( nodes[4],2, isDirected = True)
nodes[4].addEdge( nodes[2],4, isDirected = True)
nodes[4].addEdge( nodes[5],3, isDirected = True)
nodes[5].addEdge( nodes[6],4, isDirected = True)
print(go(0,6,nodes))
