
def printGrid(charsPerEdge, numBoxes):
    if charsPerEdge <= 0 or numBoxes <= 0: return None
    numVertices = numBoxes + 1
    print(drawVerticesAndEdges(
        numVertices,
        drawVerticesAndEdges(numVertices, '* ', charsPerEdge, '- '),
        charsPerEdge,
        drawVerticesAndEdges(numVertices, '| ', charsPerEdge, '  ')))

def drawVerticesAndEdges(numVertices, vertexChar, numCharsPerEdge, nonVertexChar):
    row = ''
    # If n vertices and m chars per edge then there will be n * m + 1 chars (+1 for the last vertex)
    totalChars = numVertices * numCharsPerEdge + 1
    for i in range(totalChars):
        if (i == totalChars - 1) or (i % numVertices == 0): 
            row += vertexChar
        else: 
            row += nonVertexChar
    return row + '\n'