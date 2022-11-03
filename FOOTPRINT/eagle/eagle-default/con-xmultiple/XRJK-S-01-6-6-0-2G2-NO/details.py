
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "con-xmultiple"
    oIndex = "XRJK-S-01-6-6-0-2G2-NO"
    hexID = "FZECONXMULTIPLEXRJKS1662G2NO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('con-xmultiple : XRJK-S-01-6-6-0-2G2-NO')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

