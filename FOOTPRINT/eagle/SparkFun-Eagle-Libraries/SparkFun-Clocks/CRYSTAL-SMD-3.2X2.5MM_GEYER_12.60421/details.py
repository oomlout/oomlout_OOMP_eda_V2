
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "SparkFun-Eagle-Libraries"
    oDesc = "SparkFun-Clocks"
    oIndex = "CRYSTAL-SMD-3.2X2.5MM_GEYER_12.60421"
    hexID = "FZSCLXSM32X25GEYER126421"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun-Clocks : CRYSTAL-SMD-3.2X2.5MM_GEYER_12.60421')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

