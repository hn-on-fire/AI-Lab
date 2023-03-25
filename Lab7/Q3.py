def cost(mat):
    #print(mat)
    cost = 0;
    for i in range(3):
        for j in range(3):
            if mat[i][j] != (i*3 + j + 1):
                cost += 1
    return cost -1 

mat = [[1,2,3],[0, 4, 6],[7,5,8]]
inx = (1,0)
from queue import PriorityQueue
import copy
print(mat)
while(cost(mat)!=0):
    q = PriorityQueue()
    indx = [(inx[0]+1,inx[1]),(inx[0]-1, inx[1]), (inx[0], inx[1]+1), (inx[0], inx[1]-1)]
    for i in indx:
        if i[0]<0 or i[0]>2 or i[1]<0 or i[1]>2:
            continue;
        add = copy.deepcopy(mat)
        add[inx[0]][inx[1]], add[i[0]][i[1]] = add[i[0]][i[1]], add[inx[0]][inx[1]]
        q.put((cost(add), add,i))
    a = q.get()
    mat = a[1]
    inx  = a[2]
    print(str(mat) + str(cost(mat)))
