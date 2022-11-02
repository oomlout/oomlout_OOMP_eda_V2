
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "led-lumiled"
    oIndex = "LUXEON_REBEL+COOLPAD"
    hexID = "FZELLUMLUXEONREBEL+COOLPAD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('led-lumiled : LUXEON_REBEL+COOLPAD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

