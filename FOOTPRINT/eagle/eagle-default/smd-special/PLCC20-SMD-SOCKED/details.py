
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "smd-special"
    oIndex = "PLCC20-SMD-SOCKED"
    hexID = "FZESMSPECIALPLCC2SMSOCKED"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('smd-special : PLCC20-SMD-SOCKED')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

