
def printGrid(sideLen, numBoxes):
    numVertices = numBoxes + 1

    for x in range(numVertices):
        # print the top
        printSide(sideLen, numVertices)

        if x < numVertices - 1:
            row = ''
            for i in range(numVertices):
                row += '| '
                for j in range(sideLen):
                    row += ' ' * 2
            print row

def printSide(sideLen, numVertices):
    row = ''

    for i in range(numVertices):
        row += '* '
        if i < numVertices - 1:
            for j in range(sideLen):
                row += '- '
    print row

