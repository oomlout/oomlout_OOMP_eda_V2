
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "SparkFun-Eagle-Libraries"
    oDesc = "SparkFun-Connectors"
    oIndex = "DF40-XC-(X.X)-70DS-0.4V(51)"
    hexID = "FZSSPARKFUNCNSDF4XC(XX)7DS4V(51)"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun-Connectors : DF40-XC-(X.X)-70DS-0.4V(51)')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

