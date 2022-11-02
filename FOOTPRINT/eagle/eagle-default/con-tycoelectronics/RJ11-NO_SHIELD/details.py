
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "con-tycoelectronics"
    oIndex = "RJ11-NO_SHIELD"
    hexID = "FZECONTYCOELECTRONICSRJ11NOSH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('con-tycoelectronics : RJ11-NO_SHIELD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

