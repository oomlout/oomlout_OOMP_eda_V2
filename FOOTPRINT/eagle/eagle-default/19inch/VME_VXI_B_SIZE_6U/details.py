
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "19inch"
    oIndex = "VME_VXI_B_SIZE_6U"
    hexID = "FZE19INCHVMEVXIBSIZE6U"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('19inch : VME_VXI_B_SIZE_6U')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

