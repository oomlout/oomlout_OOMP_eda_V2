
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "con-xmultiple"
    oIndex = "XRJK-S-01-6-4-0-9M2"
    hexID = "FZECONXMULTIPLEXRJKS1649M2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('con-xmultiple : XRJK-S-01-6-4-0-9M2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

