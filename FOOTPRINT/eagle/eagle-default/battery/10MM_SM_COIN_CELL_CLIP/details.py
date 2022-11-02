
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "battery"
    oIndex = "10MM_SM_COIN_CELL_CLIP"
    hexID = "FZEBAT1SMCOINCELLCLIP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('battery : 10MM_SM_COIN_CELL_CLIP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

