fileReader = open("Day1/Day1.txt", "r")
textLines = fileReader.readlines()
fileReader.close()

increasedMeasurement = 0
lineNumber = 1

while lineNumber < len(textLines):
    previous = int(textLines[lineNumber -1]) 
    current =  int(textLines[lineNumber])
    if (current > previous):
        increasedMeasurement += 1
    
    lineNumber +=1

print(f"Number of increased measurements: {increasedMeasurement}")
