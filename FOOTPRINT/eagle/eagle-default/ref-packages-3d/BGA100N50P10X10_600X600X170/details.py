
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "ref-packages-3d"
    oIndex = "BGA100N50P10X10_600X600X170"
    hexID = "FZEREFPACKAGES3DBGA1N5P1X16X6X17"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ref-packages-3d : BGA100N50P10X10_600X600X170')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

