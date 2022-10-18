import numpy as np

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

def getSequenceAlignmentValue(x, y):

	## Initialization of opt(i,j) which denotes minimum alignment value with substring [1, i] in x and [1, j] in y 
	opt = np.zeros(shape = (len(x) + 1, len(y) + 1))

	## Setting up base conditions 
	opt[:, 0] = [i*delta for i in range(0, len(x) + 1)]
	opt[0, :] = [i*delta for i in range(0, len(y) + 1)]

	## Recurrence relation computation
	for i in range(1, len(x) + 1):
		for j in range(1, len(y) + 1):
			opt[i][j] = min(alpha[convert(x[i-1])][convert(y[j-1])] + opt[i-1][j-1], delta + min(opt[i-1][j], opt[i][j-1]))

	## returning final optimal alignment value
	return opt[len(x)][len(y)]

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

def getEfficientAlignmentValue(x, y):

	## Base case
	if (len(x)<=2 or len(y)<=2):
		return getSequenceAlignmentValue(x, y)

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
	left = getEfficientAlignmentValue(x_l, y[:ind])
	right = getEfficientAlignmentValue(x_r, y[ind:])

	## merge and return
	return left + right

## Constraints
delta = 30
alpha = np.array([[0, 110, 48, 94], 
	[110, 0, 118, 48], 
	[48, 118, 0, 110],
	[94, 48, 110, 0]])

## Sample Input
s = "ACTG"
t = "TACG"
a = [3, 6, 1, 1]
b = [1, 2, 9, 2]

## Generating strings
x = generate_string(s, a)
y = generate_string(t, b)

print("Minimum Alignment Value - Basic DP: ", getSequenceAlignmentValue(x, y))
print("Minimum Alignment Value - Optimized memory DP and D&C: ", getEfficientAlignmentValue(x, y))