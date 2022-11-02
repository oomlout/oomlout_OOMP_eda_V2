
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "Adafruit-Eagle-Library"
    oDesc = "adafruit"
    oIndex = "1X25-CB"
    hexID = "FZA1X25CB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('adafruit : 1X25-CB')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

