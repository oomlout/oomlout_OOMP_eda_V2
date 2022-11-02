
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "infineon-tricore"
    oIndex = "P-BGA-388-2"
    hexID = "FZEINFINEONTRICOREPBGA3882"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('infineon-tricore : P-BGA-388-2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

