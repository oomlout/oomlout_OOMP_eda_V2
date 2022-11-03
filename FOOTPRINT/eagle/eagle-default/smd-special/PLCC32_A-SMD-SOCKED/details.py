
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "smd-special"
    oIndex = "PLCC32_A-SMD-SOCKED"
    hexID = "FZESMSPECIALPLCC32ASMSOCKED"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('smd-special : PLCC32_A-SMD-SOCKED')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

