
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "con-phoenix-500"
    oIndex = "MSTBV_2,5_13-G"
    hexID = "FZECONPHOENIX5MSTBV2513G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('con-phoenix-500 : MSTBV_2,5_13-G')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

