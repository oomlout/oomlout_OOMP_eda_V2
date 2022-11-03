
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "IQD-Frequency-Products"
    oIndex = "7.0X5.0-10-PAD"
    hexID = "FZEIQDFREQUENCYPRODUCTS7X51PAD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('IQD-Frequency-Products : 7.0X5.0-10-PAD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

