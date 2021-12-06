fileReader = open("Day2/Text.txt", "r")
textLines = fileReader.readlines()
fileReader.close()

horizontalPosition = 0
verticalPosition = 0
aim = 0

for line in textLines:
    lineInfo = line.split(' ')
    direction = lineInfo[0]
    distance = int(lineInfo[1])
    
    if(direction == 'up'):
        aim -= distance
    elif(direction == 'down'):
        aim += distance
    else:
        horizontalPosition += distance
        verticalPosition = verticalPosition + aim * distance

print(f"Final position\nDepth: {verticalPosition}\nHorizontal position: {horizontalPosition}")
print(f"Multiplied: {horizontalPosition*verticalPosition}")