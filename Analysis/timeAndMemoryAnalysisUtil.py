from resource import *
import time
import psutil
import os
import numpy as np
import matplotlib.pyplot as plt

def process_memory():
	process = psutil.Process()
	memory_info = process.memory_info()
	memory_consumed = int(memory_info.rss/1024)
	return memory_consumed

def generate_string(s, indicesList):
	for i in indicesList:
		s = s[:i+1] + s + s[i+1:]
	return s

def convert(ch):
	if (ch == 'A'):
		return 0
	elif (ch == 'C'):
		return 1
	elif (ch == 'G'):
		return 2
	elif (ch == 'T'):
		return 3

def getSequenceAlignment(x, y):

	## Initialization of opt(i,j) which denotes minimum alignment value with substring [1, i] in x and [1, j] in y 
	opt = np.zeros(shape = (len(x) + 1, len(y) + 1))

	## Setting up base conditions 
	opt[:, 0] = [i*delta for i in range(0, len(x) + 1)]
	opt[0, :] = [i*delta for i in range(0, len(y) + 1)]

	## Recurrence relation computation
	for i in range(1, len(x) + 1):
		for j in range(1, len(y) + 1):
			opt[i][j] = min(alpha[convert(x[i-1])][convert(y[j-1])] + opt[i-1][j-1], delta + min(opt[i-1][j], opt[i][j-1]))

	# Reconstructing the solution
	i = len(x); j = len(y)
	reconstructedX = ""
	reconstructedY = ""
     
	while (i > 0 and j > 0):
		if x[i - 1] == y[j - 1]:       
			reconstructedX += x[i - 1]
			reconstructedY += y[j - 1]
			i -= 1
			j -= 1
		elif (opt[i - 1][j - 1] + alpha[convert(x[i-1])][convert(y[j-1])]) == opt[i][j]:
			reconstructedX += x[i - 1]
			reconstructedY += y[j - 1]
			i -= 1
			j -= 1
		elif (opt[i][j - 1] + delta) == opt[i][j]:       
			reconstructedX += '_'
			reconstructedY += y[j - 1]
			j -= 1
		elif (opt[i - 1][j] + delta) == opt[i][j]:
			reconstructedX += x[i - 1]
			reconstructedY += '_'
			i -= 1
		
 
	while i > 0:
		reconstructedX += x[i-1]
		reconstructedY += '_'
		i -= 1

	while j > 0:
		reconstructedY += y[j-1]
		reconstructedX += '_'
		j -= 1

	return opt[len(x)][len(y)], reconstructedX[::-1], reconstructedY[::-1]

def findOptimalSolution(x, y):

	## Initialization of opt(i,j) which denotes minimum alignment value with substring [1, i] in x and [1, j] in y 
	opt = np.zeros(shape = (2, len(y) + 1))

	## Setting up base conditions
	opt[0, :] = [i*delta for i in range(0, len(y) + 1)]

	## Recurrence relation computation with just 2 columns at any point of time
	for i in range(1, len(x) + 1):
		opt[1][0] = i*delta
		prev = opt[1][0]
		for j in range(1, len(y) + 1):
			opt[1][j] = min(alpha[convert(x[i-1])][convert(y[j-1])] + opt[0][j-1], delta + min(opt[0][j], opt[1][j-1]))
			opt[0][j-1] = prev
			prev = opt[1][j]
		opt[0][len(y)] = prev
	
	## returning last column of the array
	return opt[1]

def getEfficientAlignment(x, y):

	## Base case
	if (len(x)<=2 or len(y)<=2):
		return getSequenceAlignment(x, y)

	## Dividing problem set in half and check for x_l and entire y
	x_l = x[:int(len(x)/2)]
	x_r = x[int(len(x)/2):] 
	optA = findOptimalSolution(x_l, y)

	## Compute minimum alignment value for the remaining part of the string i.e. x_r and entire y
	reverse_x_r = x_r[::-1]
	reverse_y = y[::-1]
	optB = findOptimalSolution(reverse_x_r, reverse_y)

	## Figuring out optimal index to cut the y in two parts
	opt = np.sum([optA, optB[::-1]], axis=0)
	ind = np.argmin(opt)

	## conquer part
	left = getEfficientAlignment(x_l, y[:ind])
	right = getEfficientAlignment(x_r, y[ind:])

	## merge and return
	return left[0] + right[0], left[1] + right[1], left[2] + right[2] 


# Constraints
delta = 30
alpha = np.array([[0, 110, 48, 94], 
				  [110, 0, 118, 48], 
				  [48, 118, 0, 110],
				  [94, 48, 110, 0]])