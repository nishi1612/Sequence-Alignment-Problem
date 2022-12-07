import matplotlib.pyplot as plt
import os
import re

def readFile(f):
    k = 0
    l = 0
    mem = 0
    time = 0
    lines = f.readlines()
    for line in lines:
        if (line[-1] == '\n'):
            line = line[:-1]
        if (k > 0 and k < 3): 
            l += len(line.replace('_', ''))
        elif (k == 3):
            time = float(line)
        elif (k == 4):
            mem = float(line)
        k += 1

    return l, mem, time

basicMemory = []
basicTime = []
efficientMemory = []
efficientTime = []
length = []

fb = open("basic_output.csv", 'w')
fe = open("efficient_output.csv", 'w')

x = os.listdir("./datapoints_output_basic")
x.sort(key=lambda f: int(re.sub('\D', '', f)))
for file in x:
    f = open("./datapoints_output_basic/" + file, 'r')
    l, bm, bt = readFile(f)
    basicMemory.append(bm)
    basicTime.append(bt)
    length.append(l)
    fb.write(str(l) + "," + str(bm) + "," + str(bt) + '\n')

x = os.listdir("./datapoints_output_efficient")
x.sort(key=lambda f: int(re.sub('\D', '', f)))
for file in x:
    f = open("./datapoints_output_efficient/" + file, 'r')
    l, em, et = readFile(f)
    efficientMemory.append(em)
    efficientTime.append(et)
    fe.write(str(l) + "," + str(em) + "," + str(et) + '\n')

fig1 = plt.figure(figsize=(10,6))
plt.plot(length, efficientTime)
plt.plot(length, basicTime)
plt.legend(['Efficient algorithm time consumed', 'Basic algorithm time consumed'])
plt.xlabel('Total length of string (m+n)')
plt.ylabel('Time consumed (ms)')
plt.title('Input Size vs Time Consumed')
plt.grid()
plt.savefig('timeComparision.png')

fig2 = plt.figure(figsize=(10,6))
plt.plot(length, efficientMemory)
plt.plot(length, basicMemory)
plt.legend(['Efficient algorithm memory usage', 'Basic algorithm memory usage'])
plt.xlabel('Total length of string (m+n)')
plt.ylabel('Memory usage (KB)')
plt.title('Input Size vs Memory Consumed')
plt.grid()
plt.savefig('memmoryComparision.png')
