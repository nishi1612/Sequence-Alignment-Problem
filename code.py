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

delta = 30
alpha = np.array([[0, 110, 48, 94], 
	[110, 0, 118, 48], 
	[48, 118, 0, 110],
	[94, 48, 110, 0]])

def getSequenceAlignmentValue(x, y):

	opt = np.zeros(shape = (len(x) + 1, len(y) + 1))

	opt[0][0] = 0
	for i in range(1, len(x)+1):
		opt[i][0] = opt[i-1][0] + delta

	for i in range(1, len(y)+1):
		opt[0][i] = opt[0][i-1] + delta

	for i in range(1, len(x) + 1):
		for j in range(1, len(y) + 1):
			opt[i][j] = min(alpha[convert(x[i-1])][convert(y[j-1])] + opt[i-1][j-1], delta + min(opt[i-1][j], opt[i][j-1]))

	return opt[len(x)][len(y)]

s = "ACTG"
t = "TACG"
a = [3, 6, 1, 1]
b = [1, 2, 9, 2]

x = generate_string(s, a)
y = generate_string(t, b)

print(getSequenceAlignmentValue(x, y))