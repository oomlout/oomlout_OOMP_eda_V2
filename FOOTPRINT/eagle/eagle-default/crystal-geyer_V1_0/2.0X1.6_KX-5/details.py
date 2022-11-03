
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "crystal-geyer_V1_0"
    oIndex = "2.0X1.6_KX-5"
    hexID = "FZEXGEYERV12X16KX5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('crystal-geyer_V1_0 : 2.0X1.6_KX-5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

