import numpy as np
import operator
import piecesinfo
import view
from math import *
import copy


def UpdateState(state, num, position):
#	for i in lonpospiece.possible_position:
	statenew =  copy.deepcopy(state)
	for point in position:
		statenew.point[point[0],point[1],point[2]] = num
	statenew.block[num] = True
	return statenew

class State:
	"""金字塔的状态"""
	def __init__(self):
		self.point = np.zeros([5,5,5], dtype = int)
		self.point[:] = -1
		self.point.astype(int)
		#是否使用积木
		self.block = np.zeros(12, dtype = bool)
		

#绕(0,sqrt(2)/2,sqrt(2)/2)选择90度
def Rotate1(subject):
	rot = [
	[0,-sqrt(2)/2,sqrt(2)/2],
	[sqrt(2)/2,1/2,1/2],
	[-sqrt(2)/2,1/2,1/2]
	]
	temp =[]
	for i in subject:
		temp.append(np.dot(rot,i).tolist())
	return temp

#绕(1,0,0)旋转90度
def Rotate2(subject):
	rot = [
	[1,0,0],
	[0,0,1],
	[0,-1,0]
	]
	temp =[]
	for i in subject:
		temp.append(np.dot(rot,i).tolist())
	return temp

#绕(0,0,1)旋转180度
def Rotate3(subject):
	rot = [
	[-1,0,0],
	[0,-1,0],
	[0,0,1]
	]
	temp =[]
	for i in subject:
		temp.append(np.dot(rot,i).tolist())
	return temp

class lonpospiece(object):
	"""docstring for lonpospiece"""
	def __init__(self, number, poss):
		self.num = number
		self.name = piecesinfo.allpieces[number]["name"]
		self.possible_position = poss

def ChangeToInt(piece):
	"""把坐标变为整数"""
	temp = []
	for element in piece:
		i = element[0]
		j = element[1]
		k = element[2]
		i = round(i/(sqrt(2)/2))
		j = round(j - 0.5*i)
		k = round(k - 0.5*i)
		temp.append([i,j,k])
	return temp

def IsFit(piece):
	flag = 1
	for p in piece:
		if p[0]<0 or p[0]>4 or p[1]<0 or p[1]>4-p[0] or p[2]<0 or p[2]>4-p[0]:
			flag = 0		
	return flag


def Possible(piece):
	piecepossible = []
	piece = Rotate1(piece)
	for rot1 in range(4):
		piece = Rotate1(piece)
		for rot2 in range(4):
			piece = Rotate2(piece)		
			for rot3 in range(4):
				piece = Rotate3(piece)		
				for i in range(5):
					for j in range(5-i):
						for k in range(5-i):
							temppiece = []
							for p in piece:
								temppiece.append((np.array(p) + np.array([i*sqrt(2)/2,j+i*0.5,k+i*0.5])).tolist())
					
							temppiece = ChangeToInt(temppiece)
							if IsFit(temppiece):
								piecepossible.append(temppiece)
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

'''


for i in Possible(piecesinfo.YELLOW5):
	print(i)
print(len(Possible(piecesinfo.YELLOW5)))
'''

def CanPutIn(state, position, num):
	flag = 1
	for point in position:
		if state.point[point[0],point[1],point[2]] > -1:
			flag = 0
	return flag

def IsFinished(state):
	flag = 1
	for block in state.block:
		if block == False:
			flag = 0
	return flag

def UpdagePossible(lonpos_possible, position):
	for point in position:
		for i in range(12):
			for p in lonpos_possible[i].possible_position:
				if point in p:
					del lonpos_possible[i].possible_position[p]
	return lonpos_possible

def Solve(state,lonpos_possible):
	"""求解"""
	for lonpospiece in lonpos_possible:
		num = lonpospiece.num
		if state.block[num]:
			continue
		for position in lonpospiece.possible_position:
			if CanPutIn(state, position, num):
				statenew = UpdateState(state, num, position)
				if IsFinished(statenew):
					view.View(statenew)
					os._exit()
				# UpdagePossible(lonpos_possible,position)
				Solve(statenew, lonpos_possible)

'''

Possible(piecesinfo.YELLOW5)

for i in Possible(piecesinfo.YELLOW5):
	state = State()
	state = UpdateState(state, 0, i)
	view.View(state)

'''

lonpos_possible = []
for i in range(12):
	lonpos_possible.append(lonpospiece(i, Possible(piecesinfo.allpieces[i]["coords"])))
	# print(piecesinfo.allpieces[i]["name"])
	# print(len(Possible(piecesinfo.allpieces[i]["coords"])))
	# for j in Possible(piecesinfo.allpieces[i]["coords"]):
	# 	print(j)


state = State()

# view.View(state)

Solve(state, lonpos_possible)