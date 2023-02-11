class Graph:
	elements = {}
	def __init__(self, node, edges):
		self.elements[node] = edges

	def addEdge(self, node ,edge):
		if node in self.elements.keys():
			self.elements[node] += edge
		else:
			self.elements[node] = edge
	def getAdjencyList(self):
		return self.elements
	def getAdjencyMatrix(self):
		keys = list(self.elements.keys())
		keys.sort()
		ret =  [[0] * len(keys) for i in range(len(keys))]
		for k in range(len(keys)):
			for j in self.elements[keys[k]]:
				ret[k][keys.index(j)] = 1
		return ret

if __name__ == "__main__":
	g =Graph("A",["B","C", "E"])
	g.addEdge('C',["A","B","D","E"])
	g.addEdge("B",["A",'C',"D"])
	g.addEdge("E",["A","C"])
	g.addEdge("D",["B","C"])
	print(g.getAdjencyList())
	print()
	print(g.getAdjencyMatrix())