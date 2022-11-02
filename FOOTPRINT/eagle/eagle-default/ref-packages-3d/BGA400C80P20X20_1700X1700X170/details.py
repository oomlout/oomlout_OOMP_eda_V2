
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "ref-packages-3d"
    oIndex = "BGA400C80P20X20_1700X1700X170"
    hexID = "FZEREFPACKAGES3DBGA4C8P2X217X17X17"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ref-packages-3d : BGA400C80P20X20_1700X1700X170')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

