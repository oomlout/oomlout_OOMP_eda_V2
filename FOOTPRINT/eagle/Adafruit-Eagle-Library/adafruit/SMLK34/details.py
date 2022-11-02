
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "Adafruit-Eagle-Library"
    oDesc = "adafruit"
    oIndex = "SMLK34"
    hexID = "FZASMLK34"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('adafruit : SMLK34')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

