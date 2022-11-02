
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "SparkFun-Eagle-Libraries"
    oDesc = "SparkFun-GPS"
    oIndex = "NEO-M9N_M8T_M8U_D9S"
    hexID = "FZSGNEOM9NM8TM8UD9S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun-GPS : NEO-M9N_M8T_M8U_D9S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

