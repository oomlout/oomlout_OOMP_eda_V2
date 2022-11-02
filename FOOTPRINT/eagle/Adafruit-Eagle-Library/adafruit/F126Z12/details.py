
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "Adafruit-Eagle-Library"
    oDesc = "adafruit"
    oIndex = "F126Z12"
    hexID = "FZAF126Z12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('adafruit : F126Z12')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

