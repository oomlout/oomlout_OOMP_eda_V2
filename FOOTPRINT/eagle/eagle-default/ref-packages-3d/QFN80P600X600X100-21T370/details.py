
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "ref-packages-3d"
    oIndex = "QFN80P600X600X100-21T370"
    hexID = "FZEREFPACKAGES3DQFN8P6X6X121T37"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ref-packages-3d : QFN80P600X600X100-21T370')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

