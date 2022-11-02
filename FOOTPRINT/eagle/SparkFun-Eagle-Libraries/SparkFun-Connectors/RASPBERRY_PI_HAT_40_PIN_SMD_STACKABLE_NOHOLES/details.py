
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "SparkFun-Eagle-Libraries"
    oDesc = "SparkFun-Connectors"
    oIndex = "RASPBERRY_PI_HAT_40_PIN_SMD_STACKABLE_NOHOLES"
    hexID = "FZSSPARKFUNCNSRASPBERRYPIHAT4PINSMSTACKABLENOH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun-Connectors : RASPBERRY_PI_HAT_40_PIN_SMD_STACKABLE_NOHOLES')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

