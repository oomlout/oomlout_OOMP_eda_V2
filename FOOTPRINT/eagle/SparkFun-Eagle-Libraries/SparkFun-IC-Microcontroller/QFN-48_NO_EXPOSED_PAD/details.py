
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "SparkFun-Eagle-Libraries"
    oDesc = "SparkFun-IC-Microcontroller"
    oIndex = "QFN-48_NO_EXPOSED_PAD"
    hexID = "FZSIUQFN48NOEXPOSEDPAD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun-IC-Microcontroller : QFN-48_NO_EXPOSED_PAD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

