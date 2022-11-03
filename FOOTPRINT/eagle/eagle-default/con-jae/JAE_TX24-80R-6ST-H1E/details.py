
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "con-jae"
    oIndex = "JAE_TX24-80R-6ST-H1E"
    hexID = "FZECONJAEJAETX248R6STH1E"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('con-jae : JAE_TX24-80R-6ST-H1E')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

