
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "con-cpci"
    oIndex = "044579_HI_CURRENT_PRESS"
    hexID = "FZECONCPCI44579HICURRENTPRESS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('con-cpci : 044579_HI_CURRENT_PRESS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

