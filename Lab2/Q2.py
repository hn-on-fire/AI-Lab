from Q1 import *
if __name__ == "__main__":
	nodes = []
	for i in range(6):
		nodes = nodes  + [Node(i)]
	nodes[0].addEdge( nodes[1],6, isDirected = True)
	nodes[1].addEdge( nodes[2],7, isDirected = True)
	nodes[2].addEdge( nodes[0],5, isDirected = True)
	nodes[3].addEdge( nodes[2],10, isDirected = True)
	nodes[2].addEdge( nodes[1],4, isDirected = True)
	nodes[4].addEdge( nodes[5],1, isDirected = True)
	nodes[5].addEdge( nodes[4],3, isDirected = True)
	for node in nodes:
		print(node)