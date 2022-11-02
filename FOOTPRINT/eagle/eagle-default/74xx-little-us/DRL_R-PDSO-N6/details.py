
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "74xx-little-us"
    oIndex = "DRL_R-PDSO-N6"
    hexID = "FZE74XXLITTLEUSDRLRPDSON6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('74xx-little-us : DRL_R-PDSO-N6')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

