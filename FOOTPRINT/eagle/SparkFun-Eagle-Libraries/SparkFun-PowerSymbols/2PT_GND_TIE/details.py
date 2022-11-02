
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "SparkFun-Eagle-Libraries"
    oDesc = "SparkFun-PowerSymbols"
    oIndex = "2PT_GND_TIE"
    hexID = "FZSSPARKFUNPOWERSYS2PTGNDTIE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun-PowerSymbols : 2PT_GND_TIE')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

