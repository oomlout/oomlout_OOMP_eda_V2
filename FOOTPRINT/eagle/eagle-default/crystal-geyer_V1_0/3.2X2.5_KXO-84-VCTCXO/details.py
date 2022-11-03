
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "crystal-geyer_V1_0"
    oIndex = "3.2X2.5_KXO-84-VCTCXO"
    hexID = "FZEXGEYERV132X25KXO84VCTCXO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('crystal-geyer_V1_0 : 3.2X2.5_KXO-84-VCTCXO')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

