
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "con-phoenix-smkdsp"
    oIndex = "SMKDSP_1,5_12"
    hexID = "FZECONPHOENIXSMKDSPSMKDSP1512"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('con-phoenix-smkdsp : SMKDSP_1,5_12')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

