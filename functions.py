from math import *
import numpy as np

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

#绕(0,-1,1)旋转90度
def Rotate3(subject):
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
