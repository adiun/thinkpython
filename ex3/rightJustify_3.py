
def right_justify(str):
    width = 70
    originalLen = len(str)
    numSpaces = width - originalLen
    return (numSpaces * ' ') + str

print right_justify('allen')
    
