
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "texas-sn55-sn75"
    oIndex = "D_R-PDSO-G8"
    hexID = "FZETEXASSN55SN75DRPDSOG8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('texas-sn55-sn75 : D_R-PDSO-G8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

