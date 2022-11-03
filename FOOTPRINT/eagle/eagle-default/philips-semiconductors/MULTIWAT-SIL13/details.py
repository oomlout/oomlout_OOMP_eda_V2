
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "philips-semiconductors"
    oIndex = "MULTIWAT-SIL13"
    hexID = "FZEPHILIPSSEMICONDUCTORSMULTIWATSIL13"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('philips-semiconductors : MULTIWAT-SIL13')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

