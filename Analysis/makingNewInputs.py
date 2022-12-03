import random

random.seed(a=2)
validString = "AGCT"
k = 16
for i in range(2048, 10400, 1024):
    inputString1 = ""
    inputString2 = ""
    for j in range(i):
        idx = random.randint(0, 3)
        inputString1 += validString[idx]
        idx = random.randint(0, 3)
        inputString2 += validString[idx]

    file1 = open("./newDatapoints/in" + str(k) + ".txt", "w")  
    k += 1
    file1.write(inputString1 + '\n')
    file1.write(inputString2)
    file1.close()

