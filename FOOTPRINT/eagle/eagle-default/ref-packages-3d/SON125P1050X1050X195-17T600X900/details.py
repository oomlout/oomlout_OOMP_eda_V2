
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "ref-packages-3d"
    oIndex = "SON125P1050X1050X195-17T600X900"
    hexID = "FZEREFPACKAGES3DSON125P15X15X19517T6X9"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ref-packages-3d : SON125P1050X1050X195-17T600X900')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

