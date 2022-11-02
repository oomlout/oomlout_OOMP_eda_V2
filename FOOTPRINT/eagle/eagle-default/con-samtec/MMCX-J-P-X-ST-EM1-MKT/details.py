
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "con-samtec"
    oIndex = "MMCX-J-P-X-ST-EM1-MKT"
    hexID = "FZECONSAMTECCXJPXSTEM1MKT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('con-samtec : MMCX-J-P-X-ST-EM1-MKT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

