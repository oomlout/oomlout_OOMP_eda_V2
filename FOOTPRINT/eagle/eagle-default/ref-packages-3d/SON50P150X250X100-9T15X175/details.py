
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "ref-packages-3d"
    oIndex = "SON50P150X250X100-9T15X175"
    hexID = "FZEREFPACKAGES3DSON5P15X25X19T15X175"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ref-packages-3d : SON50P150X250X100-9T15X175')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

