
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "SparkFun-Eagle-Libraries"
    oDesc = "SparkFun-Clocks"
    oIndex = "CRYSTAL-TCXO-SMD-1.65X1.25"
    hexID = "FZSCLXTCXOSM165X125"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun-Clocks : CRYSTAL-TCXO-SMD-1.65X1.25')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

