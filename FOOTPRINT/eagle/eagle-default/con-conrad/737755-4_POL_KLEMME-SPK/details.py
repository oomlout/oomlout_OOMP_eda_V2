
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "con-conrad"
    oIndex = "737755-4_POL_KLEMME-SPK"
    hexID = "FZECONCONRAD7377554POLKLEESPK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('con-conrad : 737755-4_POL_KLEMME-SPK')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

