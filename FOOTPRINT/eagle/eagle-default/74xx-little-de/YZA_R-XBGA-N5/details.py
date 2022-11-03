
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "74xx-little-de"
    oIndex = "YZA_R-XBGA-N5"
    hexID = "FZE74XXLITTLEDEYZARXBGAN5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('74xx-little-de : YZA_R-XBGA-N5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

