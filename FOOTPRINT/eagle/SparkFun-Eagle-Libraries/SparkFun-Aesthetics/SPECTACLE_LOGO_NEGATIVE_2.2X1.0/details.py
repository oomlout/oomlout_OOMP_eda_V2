
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "SparkFun-Eagle-Libraries"
    oDesc = "SparkFun-Aesthetics"
    oIndex = "SPECTACLE_LOGO_NEGATIVE_2.2X1.0"
    hexID = "FZSASPECTACLELNEGATIVE22X1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun-Aesthetics : SPECTACLE_LOGO_NEGATIVE_2.2X1.0')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

