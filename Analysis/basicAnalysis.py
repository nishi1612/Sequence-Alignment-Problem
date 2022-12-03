from resource import *
import time
import sys
import timeAndMemoryAnalysisUtil as tma

f = open(sys.argv[1], 'r')
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
        
x = tma.generate_string(inputStrings[0], a)
y = tma.generate_string(inputStrings[1], b)

## Main Driver
start_time = time.time()
tma.getSequenceAlignment(x, y)
memory_taken_basic = tma.process_memory()
end_time = time.time()
time_taken_basic = (end_time - start_time)*1000
    
file1 = open("basic_output.txt", "a")  
file1.write(str(len(x) + len(y)) + ' ' + str(time_taken_basic) + ' ' +  str(memory_taken_basic) + '\n')
file1.close()
print("Completed output for basic: " + sys.argv[1])