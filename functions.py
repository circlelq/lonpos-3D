from math import *
import numpy as np
fileObject = open('result.txt', 'w')

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

def WriteResult(state):
	for i in state:
		for j in i:
			for k in j:
			    fileObject.write(str(k)+" ")
			fileObject.write('\n')
		fileObject.write('\n')
	fileObject.write('\n')