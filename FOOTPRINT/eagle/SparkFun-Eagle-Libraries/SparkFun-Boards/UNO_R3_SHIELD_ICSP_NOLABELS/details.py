
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "SparkFun-Eagle-Libraries"
    oDesc = "SparkFun-Boards"
    oIndex = "UNO_R3_SHIELD_ICSP_NOLABELS"
    hexID = "FZSBOUNOR3SHICSPNOLABELS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun-Boards : UNO_R3_SHIELD_ICSP_NOLABELS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

