
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "74xx-little-us"
    oIndex = "DCU_R-PDSO-G8"
    hexID = "FZE74XXLITTLEUSDCURPDSOG8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('74xx-little-us : DCU_R-PDSO-G8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

