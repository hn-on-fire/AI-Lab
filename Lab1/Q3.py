def getDistances(n, x, y):
    ret = []
    for i in range(n):
        x = x+ [float(input(f'Enter x[{i}]:'))]
        y =y+ [float(input(f'Enter y[{i}]:'))]
    for i in range(n):
        ret = ret + [abs(x[i]**2 - y[i]**2)**.5]
    return ret
def bubbleSort(a):
    for i in range(len(a)-1):
        for j in range(i-1):
            if a[j+1]>a[j]:
                a[j], a[j+1] = a[j+1], a[j]
    print(a)

if __name__=="__main__":
    x = []
    y = []
    n = int(input("Enter number of values:"))
    bubbleSort(getDistances(n,x,y))
    print('done')

