class Node:
	ele = None
	lchild, rchild = None,None
	def __init__(self, ele):
		self.ele = ele
	def add(self,root, ele):

		while root != None:
			if root.ele > ele:
				if root.lchild == None:
					root.lchild = Node(ele)
					break
				root = root.lchild
			elif root.ele < ele:
				if root.rchild == None:
					root.rchild = Node(ele)
					break
				root = root.rchild
	def preOrder(self,root):
		if root == None:
			return
		print(root.ele, end = ' ')
		self.preOrder(root.lchild)
		self.preOrder(root.rchild)

	def inOrder(self,root):
		if root == None:
			return
		self.inOrder(root.lchild)
		print(root.ele, end = ' ')
		self.inOrder(root.rchild)


	def postOrder(self,root):
		if root == None:
			return
		self.postOrder(root.lchild)
		self.postOrder(root.rchild)
		print(root.ele, end = ' ')


if __name__ == '__main__':
	root = Node(25)
	root.add(root, 15)
	root.add(root, 50)
	root.add(root, 10)
	root.add(root, 22)
	root.add(root, 35)
	root.add(root, 70)
	root.add(root, 4)
	root.add(root, 12)
	root.add(root, 18)
	root.add(root, 24)
	root.add(root, 31)
	root.add(root, 44)
	root.add(root, 66)
	root.add(root, 90)
	root.preOrder(root)
	print()
	root.inOrder(root)
	print()
	root.postOrder(root)
