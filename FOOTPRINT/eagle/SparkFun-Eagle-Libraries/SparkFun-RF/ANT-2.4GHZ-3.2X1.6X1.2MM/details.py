
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "SparkFun-Eagle-Libraries"
    oDesc = "SparkFun-RF"
    oIndex = "ANT-2.4GHZ-3.2X1.6X1.2MM"
    hexID = "FZSRFANT24GHZ32X16X12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun-RF : ANT-2.4GHZ-3.2X1.6X1.2MM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

