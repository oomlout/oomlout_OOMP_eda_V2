
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "micro-renesas"
    oIndex = "P-LFQFP64-10X10"
    hexID = "FZEMRENESASPLFQFP641X1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('micro-renesas : P-LFQFP64-10X10')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

