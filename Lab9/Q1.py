from queue import Queue
q = Queue()
class Node:
    def __init__(self, param):
        if(isinstance(param,Node)):
            self.max_size = param.max_size
            self.current = param.current
        else:
            self.max_size = param;
            self.current = 0
    @classmethod
    def getChildren(cls,node):
        children = []
        temp0 = Node(node[0])
        temp1 = Node(node[1])
        temp0.current, temp1.current = min(temp0.max_size,temp0.current+temp1.current),max(0,temp1.current - (temp0.max_size-temp0.current))
        children+=[(temp0,temp1)]
        temp0 = Node(node[0])
        temp1 = Node(node[1])
        temp0.current = 0;
        children+=[(temp0,temp1)]
        temp0 = Node(node[0])
        temp1 = Node(node[1])
        temp1.current = 0;
        children+=[(temp0,temp1)]
        temp0 = Node(node[0])
        temp1 = Node(node[1])
        temp1.current, temp0.current = min(temp1.max_size,temp1.current+temp0.current),max(0,temp0.current - (temp1.max_size-temp1.current))
        children+=[(temp0,temp1)]
        temp0 = Node(node[0])
        temp1 = Node(node[1])
        temp0.current= temp0.max_size
        children+=[(temp0,temp1)]
        temp0 = Node(node[0])
        temp1 = Node(node[1])
        temp1.current= temp1.max_size
        children+=[(temp0,temp1)]
        return children
    @classmethod
    def equals(cls,a,b):
        return a.max_size==b.max_size and a.current == b.current
def printy(a):
    for i in a:
        print(i[0].current, i[1].current)
if __name__ == '__main__':
    nodes = (Node(5), Node(3))
    q.put((nodes,[]))
    explored = []
    while(True):
        curr = q.get();
        if (curr[0][0].current==2 and curr[0][0].max_size==5) or (curr[0][1].current==2 and curr[0][1].max_size==5):
            printy(curr[1])
            break;
        for child in Node.getChildren(curr[0]):
            flag =True
            for cp in explored:
                if Node.equals(cp[0],child[0]) and Node.equals(cp[1],child[1]):
                    flag = False
                    break
            if flag:
                q.put((child,curr[1]+[child]))
                explored += [child]
                #print(curr[0][0].current, curr[0][1].current)
        curr = q.get()
    