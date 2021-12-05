fileReader = open("Day2/Text.txt", "r")
textLines = fileReader.readlines()
fileReader.close()

horizontalPosition = 0
verticalPosition = 0

for line in textLines:
    lineInfo = line.split(' ')
    direction = lineInfo[0]
    distance = int(lineInfo[1])
    
    if(direction == 'up'):
        verticalPosition -= distance
    elif(direction == 'down'):
        verticalPosition += distance
    else:
        horizontalPosition += distance

print(f"Final position\nDepth: {verticalPosition}\nHorizontal position: {horizontalPosition}")
print(f"Multiplied: {horizontalPosition*verticalPosition}")