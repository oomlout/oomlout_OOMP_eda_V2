
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "Adafruit-Eagle-Library"
    oDesc = "adafruit"
    oIndex = "USB-MINIB-THM-MOLEX-PWRONLY"
    hexID = "FZAUMBTMX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('adafruit : USB-MINIB-THM-MOLEX-PWRONLY')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

