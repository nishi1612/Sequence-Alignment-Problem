import numpy as np
import sys

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

if (len(sys.argv) != 3): 
	print("Invalid number of input arguments")
	print("Input style: python3 efficient_3.py <input file> <output file>")

try:
	f = open(sys.argv[1], 'r')
except: 
	if FileNotFoundError: 
		print("No input file exists!!")

validCharacters = "ACGT"
lines = f.readlines()
inputStrings = []
a = []
b = []

for line in lines:
	if (line[-1] == '\n'):
		line = line[:-1]
	if (line[0] in validCharacters):
		inputStrings.append(line)
	else:
		if (len(inputStrings) > 2 or len(inputStrings) < 1):
			print("Invalid input file")
		elif (len(inputStrings) == 1): 
			a.append(int(line))
		else:
			b.append(int(line))

## Constraints
delta = 30
alpha = np.array([[0, 110, 48, 94], 
	[110, 0, 118, 48], 
	[48, 118, 0, 110],
	[94, 48, 110, 0]])

## Generating strings
x = generate_string(inputStrings[0], a)
y = generate_string(inputStrings[1], b)

## Main Driver
ans = getSequenceAlignment(x, y)

## opening output file
f = open(sys.argv[2], 'w')
f.write(str(ans[0]) + '\n')
f.write(str(ans[1]) + '\n')
f.write(str(ans[2]))
f.close()