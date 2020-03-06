from math import *
import numpy as np

def Rotate1(subject):
	"""绕(0,sqrt(2)/2,sqrt(2)/2)旋转90度"""
	rot = [
	[0,-sqrt(2)/2,sqrt(2)/2],
	[sqrt(2)/2,1/2,1/2],
	[-sqrt(2)/2,1/2,1/2]
	]
	temp =[]
	for i in subject:
		temp.append(np.dot(rot,i).tolist())
	return temp

def Rotate2(subject):
	"""绕(1,0,0)旋转90度"""
	rot = [
	[1,0,0],
	[0,0,1],
	[0,-1,0]
	]
	temp =[]
	for i in subject:
		temp.append(np.dot(rot,i).tolist())
	return temp

def Rotate3(subject):
	"""绕(0,-1,1)旋转90度"""
	rot = [
	[0,-sqrt(2)/2,-sqrt(2)/2],
	[sqrt(2)/2,1/2,-1/2],
	[sqrt(2)/2,-1/2,1/2]
	]
	temp =[]
	for i in subject:
		temp.append(np.dot(rot,i).tolist())
	return temp

def WriteResult(state, num):
	"""保存结果"""
	fileObject = open('results/result%04d.txt'%num, 'w')
	for i in range(5,-1,-1):
		for j in range(5-i):
			for m in range(i):
				fileObject.write(" ")
			for k in range(5-i):
				fileObject.write(str(state[i,j,k])+" ")
			fileObject.write('\n')
		fileObject.write('\n')
	fileObject.write('\n')
	fileObject.close() 

def View(state):
	"""观察摆放状态"""
	for i in range(5,-1,-1):
		for j in range(5-i):
			for m in range(i):
				print(end=" ")
			for k in range(5-i):
				print(state[i,j,k],end=" ")
			print()
	print()
