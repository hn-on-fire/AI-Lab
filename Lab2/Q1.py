class Edge:
	def __init__(self, From, To, weight = None):
		self.weight = weight
		self.edge = (From.id, To.id)
	def __str__(self): 
		cat = ',' + str(self.weight) if self.weight != None else ''
		return '(' + str(self.edge[0]) + '->' + str(self.edge[1]) + cat + ')'
class Node:
	def __init__(self, id):
		self.id = id
		self.edges = []
	def addEdge(self, To, weight = None, isDirected = False):
		self.edges +=  [str(Edge(self, To, weight))]
		if not isDirected:
			To.edges +=  Edge(To.id, self.id, weight) 
	def __str__(self):
		ret = ''
		for edge in self.edges:
			ret += str(edge)
		return ret + '\n'

if __name__ == "__main__":
	nodes = []
	for i in range(6):
		nodes = nodes  + [Node(i)]
	nodes[0].addEdge( nodes[1], isDirected = True)
	nodes[1].addEdge( nodes[2], isDirected = True)
	nodes[2].addEdge( nodes[0], isDirected = True)
	nodes[3].addEdge( nodes[2], isDirected = True)
	nodes[2].addEdge( nodes[1], isDirected = True)
	nodes[4].addEdge( nodes[5], isDirected = True)
	nodes[5].addEdge( nodes[4], isDirected = True)
	for node in nodes:
		print(node)


