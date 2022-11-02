
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "SparkFun-Eagle-Libraries"
    oDesc = "SparkFun-Electromechanical"
    oIndex = "CVS-1508_PCBSPKR"
    hexID = "FZSECVS158PCBSPKR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun-Electromechanical : CVS-1508_PCBSPKR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

