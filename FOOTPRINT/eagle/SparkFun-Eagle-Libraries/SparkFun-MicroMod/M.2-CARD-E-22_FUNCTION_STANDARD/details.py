
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "SparkFun-Eagle-Libraries"
    oDesc = "SparkFun-MicroMod"
    oIndex = "M.2-CARD-E-22_FUNCTION_STANDARD"
    hexID = "FZS2CARDE22FUNCTIONSTANDARD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun-MicroMod : M.2-CARD-E-22_FUNCTION_STANDARD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

