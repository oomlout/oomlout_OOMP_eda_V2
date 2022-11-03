
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "SparkFun-Eagle-Libraries"
    oDesc = "SparkFun-Jumpers"
    oIndex = "SMT-JUMPER_2_NO_NO-SILK_ROUND"
    hexID = "FZSSPARKFUNJSSJ2NONOSILKROUND"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun-Jumpers : SMT-JUMPER_2_NO_NO-SILK_ROUND')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

