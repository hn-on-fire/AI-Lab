import random
def h(m = 0,llimit = None, ulimit = None, step = 0.1, epochs = 1000,f = lambda x: x):
	start = random.randrange(llimit,ulimit) if llimit!= None and ulimit!=None else random.random()
	for _ in range(epochs):
		if (llimit!=None and start <llimit) or (ulimit!=None and start>ulimit) :
			return llimit if start<llimit else ulimit
		start = start+step if (f(start)>f(start+step) and m == 0 or f(start)<f(start+step) and m==1) else start-step
	return start
if __name__ == "__main__":
	print(h(1,-10,10,0.1,1000,lambda x: -x**2+5*x+10))


