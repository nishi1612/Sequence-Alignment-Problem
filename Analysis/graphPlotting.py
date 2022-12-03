import matplotlib.pyplot as plt

def readFile(f): 
    len = []
    memory = []
    time = []
    k = 0
    lines = f.readlines()
    for line in lines:

        # taking only first 15 output
        if (k > 16):
            break

        if (line[-1] == '\n'):
            line = line[:-1]
        
        words = line.split(' ')
        len.append(int(words[0]))
        memory.append(float(words[2]))
        time.append(float(words[1]))
        k += 1
    
    return len, memory, time


fb = open("basic_output.txt", 'r')
fe = open("efficient_output.txt", 'r')
len, basicMemory, basicTime = readFile(fb)
len, efficientMemory, efficientTime = readFile(fe)

fig1 = plt.figure()
plt.plot(len, efficientTime)
plt.plot(len, basicTime)
plt.legend(['Efficient algorithm time consumed', 'Basic algorithm time consumed'])
plt.xlabel('Total length of string (m+n)')
plt.ylabel('Time consumed')
plt.title('Input Size vs Time Consumed')
plt.grid()
plt.savefig('timeComparision.png')

fig2 = plt.figure()
plt.plot(len, efficientMemory)
plt.plot(len, basicMemory)
plt.legend(['Efficient algorithm memory usage', 'Basic algorithm memory usage'])
plt.xlabel('Total length of string (m+n)')
plt.ylabel('Memory usage')
plt.title('Input Size vs Memory Consumed')
plt.grid()
plt.savefig('memmoryComparision.png')