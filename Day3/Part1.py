fileReader = open("Day3/Text.txt", "r")
textLines = fileReader.readlines()
fileReader.close()

lineLength = len(textLines[0].rstrip())
numberOfLines = len(textLines)
bitDistribution = [0]*lineLength
index = 0

for line in textLines:
    trimmedLine = line.rstrip()
    for c in trimmedLine:
        bitDistribution
        bitDistribution[index] += int(c)
        index +=1
    index = 0

gammaRate = [0]*lineLength
epsilonRate = [0]*lineLength

for i in bitDistribution:
    if i > numberOfLines/2:
        gammaRate[index] = 1
        epsilonRate[index] = 0
    else:
        gammaRate[index] = 0
        epsilonRate[index] = 1
    index +=1

decimalGammaRate = 0
decimalEpsilonRate = 0

x = range(0, lineLength)

for i in x:
    decimalGammaRate += gammaRate[i]*pow(2, lineLength-1-i)
    decimalEpsilonRate += epsilonRate[i]*pow(2, lineLength-1-i)

print(f"Gamma: {decimalGammaRate}, Epsilon: {decimalEpsilonRate}")
print(f"Power consumption: {decimalGammaRate*decimalEpsilonRate}")
