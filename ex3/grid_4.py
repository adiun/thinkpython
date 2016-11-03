
def printGrid(sideLen, numBoxes):
    if sideLen <= 0: return None
    if numBoxes <= 0: return None

    numVertices = numBoxes + 1
    print(getRow(
        numVertices,
        getRow(numVertices, '* ', sideLen, '- '),
        sideLen,
        getRow(numVertices, '| ', sideLen, '  ')))

def getRow(numVertices, vertexChar, numNonVertices, nonVertexChar):
    row = ''
    for i in range(numVertices):
        row += vertexChar 
        if i < numVertices - 1:
            for j in range(numNonVertices):
                row += nonVertexChar
    return row + '\n'