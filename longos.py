import numpy as np
import operator
import piecesinfo
import view



def UpdateState(state, num, position):
#	for i in lonpospiece.possible_position:
	for point in position:
		state.a[point[0],point[1],point[2]] = num
	state.block[num] = True
	return state

class State:
	"""金字塔的状态"""
	def __init__(self):
		self.a = np.zeros([5,5,5], dtype = int)
		self.a[:] = -1
		self.a.astype(int)
		#是否使用积木
		self.block = np.zeros(12, dtype = bool)
		
state = State()



def Rotate(subject):
	rot = [
	[1,0,0],
	[0,0,1],
	[0,-1,0]
	]
	temp =[]
	for i in subject:
		temp.append(np.dot(rot,i).tolist())
	return temp

class lonpospiece(object):
	"""docstring for lonpospiece"""
	def __init__(self, num, poss):
		super(lonpospiece, self).__init__()
		num = num
		name = piecesinfo.allpieces[num]["name"]
		possible_position = poss
		


def Possible(piece):
	piecepossible = []
	for m in range(4):
		piece = Rotate(piece)
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



#for i in Possiable(GREEN4):
#	print(i)
#print(len(Possiable(GREEN4)))


#print(Rotate(whitepossible))

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

state = UpdateState(state, 1, piecesinfo.WHITE3)

view.View(state)

lonpos_possible = []
for i in range(12):
	lonpos_possible.append(lonpospiece(i, Possible(piecesinfo.allpieces[i]["coords"])))
	print(piecesinfo.allpieces[i]["name"])
	print(len(Possible(piecesinfo.allpieces[i]["coords"])))
	for j in Possible(piecesinfo.allpieces[i]["coords"]):
		print(j)




#print(state.block)








