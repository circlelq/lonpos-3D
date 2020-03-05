import numpy as np
import operator
import piecesinfo
import view
import copy
import os
from functions import *

result = 1

def UpdateState(state, num, position):
#	for i in lonpospiece.possible_position:
	statenew =  copy.deepcopy(state)
	for point in position:
		statenew[point[0],point[1],point[2]] = num
	return statenew

def GetState():
	"""金字塔的状态初始化"""
	state = np.zeros([5,5,5], dtype = int)
	state[:] = -1
	state.astype(int)
	return state

def GetPossible():
	lonpos_possible = []
	for i in range(12):
		poss = Possible(piecesinfo.allpieces[i]["coords"], piecesinfo.allpieces[i]["num"])
		lonpos_possible.append(lonpospiece(i, poss))
		# print(piecesinfo.allpieces[i]["name"])
		# print(len(poss))
		# for j in poss:
		# 	print(j)
	return lonpos_possible



class lonpospiece(object):
	"""lonpos积木类"""
	def __init__(self, number, poss):
		self.num = piecesinfo.allpieces[number]["num"]
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


def Possible(piece, num):
	piecepossible = []
	if num == 2:
		for i in range(5):
			for j in range(5-i):
				for k in range(5-i):
					temppiece = []
					for p in piece:
						temppiece.append((np.array(p) + np.array([i*sqrt(2)/2,j+i*0.5,k+i*0.5])).tolist())
			
					temppiece = ChangeToInt(temppiece)
					if IsFit(temppiece):
						piecepossible.append(temppiece)
		piece = Rotate1(piece)
		for rot2 in range(4):
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
	else:
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

def UpdatePossible(lonpos_possible, position, num):
	new = []
	for lonpospiece in lonpos_possible:
		if num == lonpospiece.num:
			continue
		newpiece = copy.deepcopy(lonpospiece)
		temp = []
		#判断是否有重合
		for p in newpiece.possible_position:
			flag = 1
			for q in position:
				if q in p:
					flag = 0
			if flag:
				temp.append(p)
		newpiece.possible_position = temp
		new.append(newpiece)
	return new

def CanSolve(state, lonpos_possible):
	flag = 1
	for i in range(5):
		for j in range(5-i):
			for k in range(5-i):
				if state[i,j,k] == -1:
					flag1 = 0
					for lonpospiece in lonpos_possible:
						for position in lonpospiece.possible_position:
							if [i,j,k] in position:
								flag1 = 1
					if flag1 == 0:
						flag = 0
	return flag


def Solve(state, lonpos_possible, left):
	"""求解"""
	if left == 0:
		global result
		WriteResult(state, result)
		result = result +1
		return
	if not CanSolve(state, lonpos_possible):
		# view.View(state)
		return
	num = lonpos_possible[0].num
	for position in lonpos_possible[0].possible_position:
		statenew = UpdateState(state, num, position)
		possiblenew = UpdatePossible(lonpos_possible, position, num)
		# view.View(statenew)
		Solve(statenew, possiblenew, left-1)

'''

Possible(piecesinfo.YELLOW5)

for i in Possible(piecesinfo.YELLOW5):
	state = State()
	state = UpdateState(state, 0, i)
	view.View(state)

'''


lonpos_possible = GetPossible()
state = GetState()

# view.View(state)

Solve(state, lonpos_possible, 12)

