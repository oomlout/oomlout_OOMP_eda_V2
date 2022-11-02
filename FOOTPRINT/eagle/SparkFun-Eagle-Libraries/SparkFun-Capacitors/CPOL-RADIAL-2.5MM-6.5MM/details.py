
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "SparkFun-Eagle-Libraries"
    oDesc = "SparkFun-Capacitors"
    oIndex = "CPOL-RADIAL-2.5MM-6.5MM"
    hexID = "FZSCCPOLR2565"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun-Capacitors : CPOL-RADIAL-2.5MM-6.5MM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

