
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "motorola-sensor-driver"
    oIndex = "MPX2050DPV"
    hexID = "FZEMOTOROLASENDRIVERMPX25DPV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('motorola-sensor-driver : MPX2050DPV')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

