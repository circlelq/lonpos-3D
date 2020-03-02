import numpy as np
import operator

def fun_1(state,i,j,k,blocks,direc):
	if blocks == 0:
		if direc == 0:
			state.a[i,j,k] = blocks
	return a

class state:
	"""金字塔的状态"""
	def __init__(self):
		self.a = np.zeros([5,5,5], dtype = int)
		self.a[:] = -1
		self.a.astype(int)
		#是否使用积木
		self.block = np.zeros(12, dtype = bool)
		
state = state()

white = [[0,0,0], [0,0,1], [0,1,1]]

def rotate(subject):
	rot = [
	[1,0,0],
	[0,0,1],
	[0,-1,0]
	]
	temp =[]
	for i in subject:
		temp.append(np.dot(rot,i).tolist())
	return temp

class Lonpospiece(object):
	"""docstring for Lonpospiece"""
	def __init__(self, name, poss):
		super(Lonpospiece, self).__init__()
		name = name
		possiable_position = poss
		


WHITE3  = [ [0,1,0], [0,0,0], [0,0,1] ]
GREEN4  = [ [0,0,0], [0,1,0], [0,1,1], [0,0,1] ]
ORANGE4 = [ [0,1,0], [0,0,0], [0,0,1], [0,0,2] ]
PURPLE4 = [ [0,0,0], [0,0,1], [0,0,2], [0,0,3] ]
BLUE5   = [ [0,1,0], [0,0,0], [0,0,1], [0,0,2], [0,0,3] ]
CYAN5   = [ [0,2,0], [0,1,0], [0,0,0], [0,0,1], [0,0,2] ]
GREEN5  = [ [0,0,0], [0,0,1], [0,0,2], [0,1,2], [0,1,3] ]
RED5    = [ [0,0,0], [0,0,1], [0,0,2], [0,1,1], [0,1,2] ]
PURPLE5 = [ [0,0,0], [0,0,1], [0,1,1], [0,1,2], [0,2,2] ]
YELLOW5 = [ [0,0,0], [0,0,1], [0,1,1], [0,2,1], [0,2,0] ]
GRAY5   = [ [0,0,1], [0,1,1], [0,1,0], [0,1,2], [0,2,1] ]
PINK5   = [ [0,0,0], [0,0,1], [0,1,1], [0,0,2], [0,0,3] ]

def possiable(piece):
	piecepossible = []
	for m in range(4):
		piece = rotate(piece)
		for i in range(5):
			for j in range(5-i):
				for k in range(5-i):
					flag = 1
					for p in piece:
						if p[0]<0 or p[0]>4 or p[1]+j<0 or p[1]+j>4-i or p[2]+k<0 or p[2]+k>4-i:
							flag = 0
					if flag:
						temp = []
						for p in piece:
							temp.append((np.array(p) + np.array([i,j,k])).tolist())
						piecepossible.append(temp)
	#去除重复项
	flag = 0
	temp = []
	for i in piecepossible:
		flag = 1
		for j in temp:
			flag1 = 0
			for k in j:
				if k not in i:
					flag1 = 1
			if flag1 == 0:
				flag = 0
		if flag:
			temp.append(i)
	return temp



for i in possiable(GREEN4):
	print(i)
print(len(possiable(GREEN4)))


#print(rotate(whitepossible))

#层数
for i in range(5):
	#横坐标
	for j in range(5-i):
		#纵坐标
		for k in range(5-i):
			if state.a[i,j,k] == -1:
				#试的积木
				for blocks in range(12):
					for direc in range(20):
						k = 10



#print(state.block)








