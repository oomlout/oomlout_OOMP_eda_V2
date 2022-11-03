
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "con-phoenix-mkds_5"
    oIndex = "MKDS_5_3-950"
    hexID = "FZECONPHOENIXMKDS5MKDS5395"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('con-phoenix-mkds_5 : MKDS_5_3-950')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

