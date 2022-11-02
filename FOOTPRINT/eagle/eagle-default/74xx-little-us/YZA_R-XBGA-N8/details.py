
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "74xx-little-us"
    oIndex = "YZA_R-XBGA-N8"
    hexID = "FZE74XXLITTLEUSYZARXBGAN8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('74xx-little-us : YZA_R-XBGA-N8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

