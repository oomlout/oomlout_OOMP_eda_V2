
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "toshiba"
    oIndex = "QFP67-P-1420-0.80"
    hexID = "FZETOSHIBAQFP67P1428"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('toshiba : QFP67-P-1420-0.80')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

