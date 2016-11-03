
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
    # If there are n vertices and m non-vertices then there will be n * m + 1 chars (+1 for the last vertex)
    # n = 3, m = 2
    # 1 2 3 4 5 6 7
    # * - - * - - *
    totalChars = numVertices * numNonVertices + 1
    for i in range(totalChars):
        if i == totalChars - 1:
            row += vertexChar
        elif i % numVertices == 0:
            row += vertexChar
        else:
            row += nonVertexChar

    return row + '\n'