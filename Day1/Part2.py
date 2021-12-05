fileReader = open("Day1/Text.txt", "r")
textLines = fileReader.readlines()
fileReader.close()

increasedMeasurement = 0
lineNumber = 1
previousWindow = 0

while lineNumber < len(textLines)-1:
    previous = int(textLines[lineNumber -1]) 
    current =  int(textLines[lineNumber])
    next = int(textLines[lineNumber+1])
    currentWindow = previous + current + next

    if (currentWindow > previousWindow and lineNumber > 1 ):
        increasedMeasurement += 1

    previousWindow = currentWindow
    lineNumber +=1

print(f"Number of increased measurements: {increasedMeasurement}")
