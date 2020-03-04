import numpy as np

def View(state):
	for i in range(5,-1,-1):
		for j in range(5-i):
			for m in range(i):
				print(end=" ")
			for k in range(5-i):
				print(state[i,j,k],end=" ")
			print()
	print()
