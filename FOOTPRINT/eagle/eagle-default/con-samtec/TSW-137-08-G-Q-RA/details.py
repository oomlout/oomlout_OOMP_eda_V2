
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "con-samtec"
    oIndex = "TSW-137-08-G-Q-RA"
    hexID = "FZECONSAMTECTSW1378GQRA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('con-samtec : TSW-137-08-G-Q-RA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

