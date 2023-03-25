V = 4
answer = []

def tsp(graph, v, currPos, n, count, cost):

    if (count == n and graph[currPos][0]):
        answer.append(cost + graph[currPos][0])
        return

    for i in range(n):
        if (v[i] == False and graph[currPos][i]):
             

            v[i] = True
            tsp(graph, v, i, n, count + 1,
                cost + graph[currPos][i])

            v[i] = False

if __name__ == '__main__':
    n = 4
    graph= [[ 0, 2, 3, 1 ],
            [ 2, 0, 4, 1 ],
            [ 3, 4, 0, 3 ],
            [ 1, 2, 3, 0 ]]
 

    v = [False for i in range(n)]
     
    v[0] = True
 
    tsp(graph, v, 0, n, 1, 0)
    print(answer)